export interface DataReader {
  read(headers?: string[]): void;
  data: string[][] | null;
  headers: string[];
}