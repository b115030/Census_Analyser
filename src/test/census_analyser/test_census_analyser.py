from src.main.census_analyser.census_analyser import read_from_csv

CENSUS_CSV_FILE_PATH = "../../../resources/StateCensusData.csv"


class Test_read_from_csv:
    def given_state_census_CSV_file_should_match_number_of_records_in_file(self):
        csv_loader = read_from_csv(CENSUS_CSV_FILE_PATH)
        assert csv_loader.lines_count() == 29
