import pandas as pd

def get_trips_fees(main_df):

    # فلترة بالوصف لو يحتوي على indrive أو uber أو didi (حساس لحالة الأحرف)
    keywords = ["indrive", "uber", "didi"]
    pattern = "(?i)" + "|".join(keywords)

    filtered_trip_df = main_df[
        main_df["Description"].str.contains(pattern, case=False, na=False)
    ]

    # تحويل عمود Debit إلى رقم بعد حذف الفواصل
    filtered_trip_df.loc[:,"Debit"] = (
        filtered_trip_df["Debit"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    # حساب الإجمالي
    return filtered_trip_df["Debit"].sum()

def get_total_fees(main_df):


    # تحويل عمود Debit إلى رقم بعد حذف الفواصل
    main_df.loc[:, "Debit"] = (
        main_df["Debit"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    # حساب المجموع
    return main_df["Debit"].sum()
def total_credit(main_df):
    # تحويل عمود Credit إلى رقم بعد إزالة الفواصل
    main_df.loc[:, "Credit"] = (
    main_df["Credit"]
    .astype(str)
    .str.replace(",", "")
    .astype(float)
)

    # حساب مجموع الدائن
    return main_df["Credit"].sum()

def load_expenses(file_path,start_date,end_date):
    # قراءة الجدول وتجاهل الصفين الأولين
    df = pd.read_excel(file_path, sheet_name=0, skiprows=2)

    # # لو حابب تتأكد من الأعمدة
    # print(df.columns)

    # تحويل عمود التاريخ لتاريخ فعلي
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # فلترة المعاملات ضمن الفترة
    return df.loc[(df["Date"] >= start_date) & (df["Date"] <= end_date)].copy()

def main():
    file_path="C:\\Users\\KareemSA\\Downloads\\OpTransactionHistoryUX529-06-2025 20_49_29.xlsx"
    start_date = pd.to_datetime("2025-05-22")
    end_date = pd.to_datetime("2025-06-29")
    main_data = load_expenses(file_path, start_date, end_date)
    print("إجمالي المبلغ المصروف :")
    print(get_total_fees(main_data))
    print("إجمالي مصروفات المواصلات :")
    print(get_trips_fees(main_data))
    print("إجمالي الدائن (Credit) في الفترة المحددة:")
    print(total_credit(main_data))

if __name__ == '__main__':
    main()