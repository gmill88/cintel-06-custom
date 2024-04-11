# Import necessary libraries
import seaborn as sns
from faicons import icon_svg
from shiny import reactive
from shiny.express import input, render, ui

tips_df = sns.load_dataset("tips")

ui.page_opts(title="Tips Dash", fillable=True)

with ui.sidebar(title="Tips Dashboard"):
    ui.input_slider("tip", "Tip", 0, 10, 10, step=.01)
    ui.input_checkbox_group(
        "sex",
        "Sex",
        ["Male", "Female"],
        selected=["Male", "Female"],
    )
    ui.input_checkbox_group(
        "smoker",
        "Smoker",
        ["Yes", "No"],
        selected=["Yes", "No"],
    )
    ui.a(
        "GitHub Source",
        href="https://github.com/gmill88/cintel-06-custom"

    )
    ui.a(
        "GitHub App",
        href="https://github.com/gmill88/cintel-06-custom/blob/main/app.py"
    )


with ui.layout_columns():
    with ui.value_box(full_screen=True):
        "Number of Transactions"

        @render.text
        def transaction_count():
            return filtered_data().shape[0]
                       
    with ui.value_box(full_screen=True):
        "Average Tip"

        @render.text
        def avg_tip():
            return f"{filtered_data()['tip'].mean():.1f} dollars"

    with ui.value_box(full_screen=True):
        ui.card_header("Average Tip Percent")

        @render.text
        def avg_tip_percent():
            filtered_df = filtered_data()  # Get the filtered DataFrame
            average_tip_percent = (filtered_df['tip'] / filtered_df['total_bill']).mean() * 100
            return f"{average_tip_percent:.2f}%"


with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Tips vs. Sex")

        @render.plot
        def age_fare():
            return sns.scatterplot(
                data=filtered_data(),
                x="tip",
                y="sex",
                hue="smoker",
            )
            

with ui.card(full_screen=True):
        ui.card_header("Passenger Data")

        @render.data_frame
        def payer_data():
            cols = [
                "total_bill",
                "tip",
                "sex",
                "smoker",
                "day",
                "time",
                "size"
            ]
            return render.DataGrid(filtered_data())
            
@reactive.calc
def filtered_data():
    tip_amount = input.tip()
    selected_sex = input.sex()
    smoker_filter = input.smoker()
    filtered_df = tips_df[
        (tips_df['tip'] <= tip_amount) &       
        (tips_df['sex'].isin(selected_sex)) &
        (tips_df['smoker'].isin(smoker_filter))
        ]    
    return filtered_df
