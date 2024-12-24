import gspread

def google_sheet(scrapped):
    google_credentials = gspread.service_account(filename="/home/mubashir/PycharmProjects/SeleniumScrapper/gspread-440812-e735a03321ad.json")
    sheet_id = google_credentials.open_by_key("1Hkk7HRZYIlvTZi_dqfhenhITLIm26OLmUIhzpO9kFwk")

    current_sheet = sheet_id.worksheet("test")

    for i, value in enumerate(scrapped, start=1):  # start=1 to start from the first row
        current_sheet.update_cell(i, 1, value)

