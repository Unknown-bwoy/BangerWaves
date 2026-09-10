import flet as ft 

main_ws_row = ft.Row(
    controls=[
        #Left Panel Component: Fixed width, takes 250 pixels of your screen 
        ft.Container(width=250,bgcolor=ft.Colors.SURFACE_CONTAINER_LOW),
        
        #Right Panel COmponents: Expands dynamically  
        ft.Container(expand=True,bgcolor=ft.Colors.BLACK)



    ],
    expand=True # Tells the Row to expand completely down to the bottom console player line 

) 


class BangerWaveLayout: 
    def __init__(self,page:ft.Page) -> None:
        self.page = page 
         #Set window theme configuration  
        self.page.theme_mode = ft.ThemeMode.DARK 
        self.page.bgcolor = ft. 