import pandas as pd


def update_excel_file(input_file, output_file):
    # Load the Excel file
    xls = pd.ExcelFile(input_file)
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

    # Define new values for the additional rows
    new_values = {
        "PermissionName": "الخدمات - عرض الطلبات المنتهية",
        "ActionId": "view-completed",
        "ActionName": "عرض الطلبات المنتهية",
        "maapingId": "",
        "ActionTechnical": "yes",
    }

    # Identify unique combinations of ServiceId, ProviderRoleId, and ProviderRoleName
    unique_combinations = df[["ServiceId", "ProviderRoleId", "ProviderRoleName"]].drop_duplicates()

    # Remove rows that already contain the new PermissionName and ActionId
    existing_rows = df[
        (df["PermissionName"] == new_values["PermissionName"]) &
        (df["ActionId"] == new_values["ActionId"])
        ]

    # Filter only the combinations that are missing from the existing rows
    missing_combinations = unique_combinations.merge(
        existing_rows[["ServiceId", "ProviderRoleId", "ProviderRoleName"]],
        on=["ServiceId", "ProviderRoleId", "ProviderRoleName"],
        how="left",
        indicator=True
    ).query('_merge == "left_only"').drop(columns=["_merge"])

    # If there are missing combinations, create new rows
    if not missing_combinations.empty:
        # Select a sample row per combination to retain structure
        sample_rows = df.merge(
            missing_combinations, on=["ServiceId", "ProviderRoleId", "ProviderRoleName"], how="inner"
        ).drop_duplicates(subset=["ServiceId", "ProviderRoleId", "ProviderRoleName"])

        # Update only the required columns
        for col, value in new_values.items():
            sample_rows[col] = value

        # Append the new rows to the original DataFrame
        df_updated = pd.concat([df, sample_rows], ignore_index=True)
    else:
        df_updated = df  # No changes needed if all rows already exist

    # Save the modified DataFrame to a new Excel file
    df_updated.to_excel(output_file, index=False)


if __name__ == '__main__':
    input_file = "E:\\Repos\\BaladyBusiness\\be-baladybusiness-files\\configs\\authorization-service\\صلاحيات منصة انجاز.xlsx"
    output_file = "E:\\Repos\\BaladyBusiness\\be-baladybusiness-files\\configs\\authorization-service\\صلاحيات_منصة_انجاز_محدث.xlsx"
    update_excel_file(input_file, output_file)


