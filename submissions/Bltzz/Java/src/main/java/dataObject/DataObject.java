package dataObject;

import com.opencsv.bean.CsvBindByPosition;

public class DataObject {

	@CsvBindByPosition(position = 0)
	private String trackName;

	@CsvBindByPosition(position = 1)
	private String artistName;

	@CsvBindByPosition(position = 2)
	private int artistCount;

	@CsvBindByPosition(position = 3)
	private int releasedYear;

	@CsvBindByPosition(position = 4)
	private String releasedMonth;

	@CsvBindByPosition(position = 5)
	private int releasedDay;

	@CsvBindByPosition(position = 6)
	private String inSpotifyPlaylists;

	@CsvBindByPosition(position = 7)
	private String inSpotifyCharts;

	@CsvBindByPosition(position = 8)
	private long streams;

	@CsvBindByPosition(position = 9)
	private String inApplePlaylists;

	@CsvBindByPosition(position = 10)
	private String inAppleCharts;

	@CsvBindByPosition(position = 11)
	private String inDeezerPlaylists;

	@CsvBindByPosition(position = 12)
	private String inDeezerCharts;

	@CsvBindByPosition(position = 13)
	private String inShazamCharts;

	@CsvBindByPosition(position = 14)
	private int bpm;

	@CsvBindByPosition(position = 15)
	private String key;

	@CsvBindByPosition(position = 16)
	private String mode;

	@CsvBindByPosition(position = 17)
	private double danceabilityPercentage;

	@CsvBindByPosition(position = 18)
	private double valencePercentage;

	@CsvBindByPosition(position = 19)
	private double energyPercentage;

	@CsvBindByPosition(position = 20)
	private double acousticnessPercentage;

	@CsvBindByPosition(position = 21)
	private double instrumentalnessPercentage;

	@CsvBindByPosition(position = 22)
	private double livenessPercentage;

	@CsvBindByPosition(position = 23)
	private double speechinessPercentage;
	// Add getters and setters

	@Override
	public String toString() {
		return "Track{" + "trackName='" + trackName + '\'' + ", artistName='" + artistName + '\'' + ", artistCount="
				+ artistCount + ", releasedYear=" + releasedYear + ", releasedMonth='" + releasedMonth + '\''
				+ ", releasedDay=" + releasedDay + ", inSpotifyPlaylists=" + inSpotifyPlaylists + ", inSpotifyCharts="
				+ inSpotifyCharts + ", streams=" + streams + ", inApplePlaylists=" + inApplePlaylists
				+ ", inAppleCharts=" + inAppleCharts + ", inDeezerPlaylists=" + inDeezerPlaylists + ", inDeezerCharts="
				+ inDeezerCharts + ", inShazamCharts=" + inShazamCharts + ", bpm=" + bpm + ", key='" + key + '\''
				+ ", mode='" + mode + '\'' + ", danceabilityPercentage=" + danceabilityPercentage
				+ ", valencePercentage=" + valencePercentage + ", energyPercentage=" + energyPercentage
				+ ", acousticnessPercentage=" + acousticnessPercentage + ", instrumentalnessPercentage="
				+ instrumentalnessPercentage + ", livenessPercentage=" + livenessPercentage + ", speechinessPercentage="
				+ speechinessPercentage + '}';
	}

	public String getTrackName() {
		return trackName;
	}

	public void setTrackName(String trackName) {
		this.trackName = trackName;
	}

	public String getArtistName() {
		return artistName;
	}

	public void setArtistName(String artistName) {
		this.artistName = artistName;
	}

	public int getArtistCount() {
		return artistCount;
	}

	public void setArtistCount(int artistCount) {
		this.artistCount = artistCount;
	}

	public int getReleasedYear() {
		return releasedYear;
	}

	public void setReleasedYear(int releasedYear) {
		this.releasedYear = releasedYear;
	}

	public String getReleasedMonth() {
		return releasedMonth;
	}

	public void setReleasedMonth(String releasedMonth) {
		this.releasedMonth = releasedMonth;
	}

	public int getReleasedDay() {
		return releasedDay;
	}

	public void setReleasedDay(int releasedDay) {
		this.releasedDay = releasedDay;
	}

	public String getInSpotifyPlaylists() {
		return inSpotifyPlaylists;
	}

	public void setInSpotifyPlaylists(String inSpotifyPlaylists) {
		this.inSpotifyPlaylists = inSpotifyPlaylists;
	}

	public String getInSpotifyCharts() {
		return inSpotifyCharts;
	}

	public void setInSpotifyCharts(String inSpotifyCharts) {
		this.inSpotifyCharts = inSpotifyCharts;
	}

	public long getStreams() {
		return streams;
	}

	public void setStreams(long streams) {
		this.streams = streams;
	}

	public String getInApplePlaylists() {
		return inApplePlaylists;
	}

	public void setInApplePlaylists(String inApplePlaylists) {
		this.inApplePlaylists = inApplePlaylists;
	}

	public String getInAppleCharts() {
		return inAppleCharts;
	}

	public void setInAppleCharts(String inAppleCharts) {
		this.inAppleCharts = inAppleCharts;
	}

	public String getInDeezerPlaylists() {
		return inDeezerPlaylists;
	}

	public void setInDeezerPlaylists(String inDeezerPlaylists) {
		this.inDeezerPlaylists = inDeezerPlaylists;
	}

	public String getInDeezerCharts() {
		return inDeezerCharts;
	}

	public void setInDeezerCharts(String inDeezerCharts) {
		this.inDeezerCharts = inDeezerCharts;
	}

	public String getInShazamCharts() {
		return inShazamCharts;
	}

	public void setInShazamCharts(String inShazamCharts) {
		this.inShazamCharts = inShazamCharts;
	}

	public int getBpm() {
		return bpm;
	}

	public void setBpm(int bpm) {
		this.bpm = bpm;
	}

	public String getKey() {
		return key;
	}

	public void setKey(String key) {
		this.key = key;
	}

	public String getMode() {
		return mode;
	}

	public void setMode(String mode) {
		this.mode = mode;
	}

	public double getDanceabilityPercentage() {
		return danceabilityPercentage;
	}

	public void setDanceabilityPercentage(double danceabilityPercentage) {
		this.danceabilityPercentage = danceabilityPercentage;
	}

	public double getValencePercentage() {
		return valencePercentage;
	}

	public void setValencePercentage(double valencePercentage) {
		this.valencePercentage = valencePercentage;
	}

	public double getEnergyPercentage() {
		return energyPercentage;
	}

	public void setEnergyPercentage(double energyPercentage) {
		this.energyPercentage = energyPercentage;
	}

	public double getAcousticnessPercentage() {
		return acousticnessPercentage;
	}

	public void setAcousticnessPercentage(double acousticnessPercentage) {
		this.acousticnessPercentage = acousticnessPercentage;
	}

	public double getInstrumentalnessPercentage() {
		return instrumentalnessPercentage;
	}

	public void setInstrumentalnessPercentage(double instrumentalnessPercentage) {
		this.instrumentalnessPercentage = instrumentalnessPercentage;
	}

	public double getLivenessPercentage() {
		return livenessPercentage;
	}

	public void setLivenessPercentage(double livenessPercentage) {
		this.livenessPercentage = livenessPercentage;
	}

	public double getSpeechinessPercentage() {
		return speechinessPercentage;
	}

	public void setSpeechinessPercentage(double speechinessPercentage) {
		this.speechinessPercentage = speechinessPercentage;
	}
}
