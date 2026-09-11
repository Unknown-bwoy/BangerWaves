import flet as ft 

#Forcing Elements to expand and back tightly side-by-side
main_ws_row = ft.Row(
    controls=[
        #Left Panel Component: Fixed width, takes 250 pixels of your screen 
        ft.Container(width=250,bgcolor=ft.Colors.SURFACE_CONTAINER_LOW),
        
        #Right Panel COmponents: Expands dynamically  
        ft.Co(expand=True,bgcolor=ft.COLORS.BLACK)



    ],
    expand=True # Tells the Row to expand completely down to the bottom console player line 

) 

#Designing a Multi-Pane Layout Partition
class BangerWaveLayout: 
    def __init__(self,page:ft.Page) -> None:
        self.page = page 
         #Set window theme configuration  
        self.page.theme_mode = ft.ThemeMode.DARK 
        self.page.bgcolor = ft.Colors.BLACK 

    def _build_sidebar(self) -> ft.Container: 
        """Return a fixed left panel container for main navigation."""
        return ft.Container(
            width=230,
            bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
            padding=15, 
            border_radius=8  

          )
             


    def _build_viewport(self) -> ft.Container: 
      """Returns a fixed bottom console container block for track timeline controls.""" 
      return ft.Container(
          height=90,
          bgcolor=ft.Colors.SURFACE_CONTAINER_HIGH, 
          padding= 15, 
          border_radius=12 

        )  

    def _build_player_bar(self) -> ft.Container: 
        """Returns a fixed bottom console container block for track timeline contols.""" 
        return ft.Container(
            expand=True,
            bgcolor=ft.Colors.BLACK,
            padding=15


        ) 


    #Assembling the Multi-Pane Window Structure 
    
    def assemble(self): 
        """Assembles and renders the full structural panel array directly into the pages framework""" 
        self.page.clean() 

        # Row layout combines the left sidebar and the sidebar and the right fluid workspace side-by-side 
        main_ws = ft.Row(
            controls=[self._build_sidebar(),self._build_viewport()],
            expand=True # Stretches the workspace row vertically to absorb 
            #all remaining screen space

        )   

        # Column layout strucks the top workspace and the fixed bottom player console vertically 
        self.page.add(
            ft.Column(
                controls=[
                    main_ws,
                    self._build_player_bar()
                ], 
                expand=True # Expands the master column down to the absolute bottom window border lines 

            )
        ) 

        #Left metadata zone  
    left_metadata_zone = ft.Container(
            content=ft.Column([
                ft.Text("No Track Selected",weight=ft.FontWeight.BOLD, size=13), 
               ft.Text("Unknown Artist",size=11,color=ft.Colors.GREY_400)
            ]), 
            width=200 # Fixed Tracking width block boundary
        ) 

        #Center timeline control console zone 
    center_playback_zone = ft.Column(
        controls=[
            ft.Row([
                ft.IconButton(icon=ft.Icons.SHUFFLE_ROUNDED, icon_size=17), 
                ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED,icon_size=36), 
                ft.IconButton(icon=ft.Icons.REPEAT_ROUNDED,icon_size=17),
         ], alignment=ft.MainAisAlignment.CENTER),
         ft.Row([
            ft.Text("0:00",size=10),
            ft.Slider(expand=True, active_color=ft.Colors.GREEN_ACCENT_400), 
            ft.Text("0:00",size=10) 
        
         ])
          
      
         ],  
         expand=True # Expands dynamically to absorb all central space between panels 
    

    )


        #Master row assembly 
    

    right_utility_zone = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.VOLUME_UP_ROUNDED,size=17), 
            ft.Slider(width=100,value=80) 
        ]),
        width=199 #Fixed utility layout space matrix  
    ) 

         #Master row assembly  
    player_conslole_bar = ft.Row(
        controls=[left_metadata_zone, center_playback_zone,right_utility_zone],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )   
    