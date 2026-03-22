from sheets import connect_sheet
from ai import generate_ai_fields

def run_bot():
    sheet = connect_sheet()

    data = sheet.get_all_records()

    print("Fetched data:", data)

    for i, row in enumerate(data, start=2):
        input_text = row.get("Input Text")
        status = row.get("Status")

        print(f"Row {i} → Input:", input_text, "| Status:", status)

        if input_text and status != "Done":
            print(f"Processing row {i}...")

            summary, tags, caption = generate_ai_fields(input_text)

            print("Summary:", summary)
            print("Tags:", tags)
            print("Caption:", caption)

            # Update sheet
            sheet.update_cell(i, 2, summary)
            sheet.update_cell(i, 3, tags)
            sheet.update_cell(i, 4, caption)
            sheet.update_cell(i, 5, "Done")

            print(f"Row {i} completed ✅")

        else:
            print(f"Row {i} skipped")

if __name__ == "__main__":
    run_bot()
