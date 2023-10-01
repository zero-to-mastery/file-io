open Cohttp_lwt_unix
open Csv

let get_response_data () =
  let url = Uri.of_string "https://api.github.com/gists/90d83765febf8e86578b4dd56fb82b54" in
  let headers = Header.init_with "User-Agent" "OCaml" in
  let%lwt response, body = Client.get ~headers url in
  let%lwt body_string = Cohttp_lwt.Body.to_string body in
  let response_data = Yojson.Safe.from_string body_string in
  let csv_content = Yojson.Safe.Util.(response_data |> member "files" |> member "spotify-2023.csv" |> member "content" |> to_string) in
  Lwt.return csv_content

let () =
  let songs = ref [] in
  let authors = Hashtbl.create 10 in

  let process_row row =
    songs := row :: !songs;
    let author = List.nth row 1 in
    if Hashtbl.mem authors author then
      let count = Hashtbl.find authors author in
      Hashtbl.replace authors author (count + 1)
    else
      Hashtbl.add authors author 1
  in

  let process_data data =
    let csv_stream = Csv.of_string ~has_header:true data in
    Csv.iter process_row csv_stream;
    let songs_count = List.length !songs in
    let e_songs_count = List.length (List.filter (fun row -> String.length (List.nth row 1) > 0 && (String.get (List.nth row 1) 0 = 'E' || String.get (List.nth row 1) 0 = 'e')) !songs) in
    let max_author, max_songs =
      Hashtbl.fold (fun author count (max_author, max_count) ->
          if count > max_count then (author, count) else (max_author, max_count)
        ) authors ("", -1)
    in
    Printf.printf "Number of Songs: %d\n" songs_count;
    Printf.printf "Number of Songs starting with E: %d\n" e_songs_count;
    Printf.printf "The author with the most songs is %s with %d songs.\n" max_author max_songs
  in

  Lwt_main.run (
    get_response_data () >>= fun response_data ->
    process_data response_data;
    Lwt.return ()
  )
