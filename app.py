# Import necessary libraries
import seaborn as sns
from faicons import icon_svg
from shiny import reactive
from shiny.express import input, render, ui
from shinyswatch import theme

theme.flatly
tips_df = sns.load_dataset("tips")
        
ui.page_opts(title="Miller Tips Dash", fillable=True)

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
    ui.input_radio_buttons("dark_mode", "Dark Mode:", ["Yes", "No"], selected="Yes")



theme_color = "#20c997"  # Blue theme color

with ui.layout_columns():
    with ui.card():
        ui.card_header("Summary")
        with ui.layout_columns():
            with ui.value_box(showcase=icon_svg("hashtag"), style=f"padding: 10px; background-color: {theme_color};"):
                "Number of Transactions"
                @render.text
                def transaction_count():
                    return filtered_data().shape[0]
            with ui.value_box(showcase=icon_svg("dollar-sign"), style=f"padding: 10px; background-color: {theme_color};"):
                "Average Tip"
                @render.text
                def avg_tip():
                    return f"${filtered_data()['tip'].mean():.1f}"

            with ui.value_box(showcase=icon_svg("percent"), style=f"padding: 10px; background-color: {theme_color};"):
                "Average Tip Percent"
                @render.text
                def avg_tip_percent():
                    filtered_df = filtered_data()
                    average_tip_percent = (filtered_df['tip'] / filtered_df['total_bill']).mean() * 100
                    return f"{average_tip_percent:.2f}%"
                    
with ui.accordion(style="background-color: #20c997;"):  
    with ui.accordion_panel("Tips Data Grid", style="background-color: #20c997;"):  
        with ui.card(full_screen=True):
            ui.card_header("Tips Data Grid")

            @render.data_frame
            def tips_data():
                return render.DataGrid(data=filtered_data(), selection_mode="rows")


with ui.layout_columns():
    with ui.card(full_screen=True, style="background-color: #20c997;"): 
        ui.card_header("Tip Percentage Based on Sex")

        @render.plot()
        def tip_sex():
            filtered_df = filtered_data()
            filtered_df['tip_percent'] = (filtered_df['tip'] / filtered_df['total_bill']) * 100  # Calculate tip percent
            return sns.violinplot(
                data=filtered_df,
                y="tip_percent",  # Use tip percent as y-axis
                x="sex",
                hue="smoker",
                split=True,
                inner="quartile",
            )
        

    with ui.card(full_screen=True, style="background-color: #20c997;"): 
        ui.card_header("Total Bill vs. Tip")

        @render.plot()
        def bill_tip():
            filtered_df = filtered_data()

            ax = sns.scatterplot(
                data=filtered_df,
                x="total_bill",
                y="tip",
            )

            ten_percent_tip = filtered_df['total_bill'] * 0.1

            ax.plot(filtered_df['total_bill'], ten_percent_tip, color='red', linestyle='--', label='10% Tip')
            ax.legend()
            
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
        
    @reactive.effect()
    def _():
        if input.dark_mode() == "Yes":
            ui.update_dark_mode("dark")
        else:
            ui.update_dark_mode("light")


