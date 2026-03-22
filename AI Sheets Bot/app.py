from ai import generate_ai_fields
from sheets import connect_sheet


def run_cli():
    print("🤖 AI Content Generator (CLI Version)")
    print("-" * 40)

    # Take user input
    user_input = input("Enter your text: ").strip()

    if not user_input:
        print("❌ Please enter valid text")
        return

    print("\n⏳ Generating...\n")

    summary, tags, caption = generate_ai_fields(user_input)

    print("✅ DONE!\n")

    print("📌 Summary:")
    print(summary)

    print("\n🏷️ Tags:")
    print(tags)

    print("\n📢 Caption:")
    print(caption)

    # Ask user to save to Google Sheets
    choice = input("\nDo you want to save to Google Sheets? (y/n): ").lower()

    if choice == "y":
        try:
            sheet = connect_sheet()
            sheet.append_row([user_input, summary, tags, caption, "Done"])
            print("✅ Saved to Google Sheets!")
        except Exception as e:
            print("❌ Error saving to sheet:", str(e))
    else:
        print("Skipped saving.")


if __name__ == "__main__":
    run_cli()
