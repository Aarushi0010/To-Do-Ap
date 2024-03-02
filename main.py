from flet import *

def main(page : Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    categories_card = Row(
        scroll = 'auto',

    )
    categories = ['Business' , 'Family' , 'Friends']
    for i,category in enumerate(categories) :
        categories_card.controls.append(
            Container(
                bgcolor = BG, height = 150,
                width = 170,border_radius = 10,
                padding = 15,
                content = Column(
                    controls = [
                        Text('40 Tasks',color = 'white',font_family='Robot Slab'),
                        Text (category,color = 'white'),
                        Container(
                           width = 160,
                           height = 5,
                           bgcolor = 'white12' ,
                           border_radius = 20,
                           padding = padding.only(right = i*30),
                           content = Container(
                               bgcolor = PINK,
                           )
                        ),
                    ],
                )
            )
        )
    
    first_page_contents = Container(
        content = Column(
            controls = [
                Row(alignment = 'spaceBetween',
                    
                    controls = [
                        Container(
                            content = Icon(
                                icons.MENU ,color = 'white')),


                    Row(
                        controls = [
                            Icon(icons.SEARCH, color = 'white'),
                            Icon(icons.NOTIFICATION_ADD_OUTLINED, color = 'white')
                        ]
                    ),
                    ],
                ),
                Container(height = 20),
                Text(
                        value = 'Hey! What\'s up',
                        color = 'white',
                        size = 26,
                    ),
                Text (
                    value = 'CATEGORIES',
                    color = 'white',
                ),
                Container (
                    padding = padding.only(top = 10, bottom = 20),
                    content = categories_card,
                ) ,   
            ],

        ),
    )
    page_1 = Container()
    page_2 = Row(
        controls = [
            Container(
                width = 400,
                height = 750,
                bgcolor = FG,
                border_radius = 38,
                padding = padding.only(
                    top = 50,left = 20, right = 20,bottom = 5
                ),
                content = Column(
                    controls = [
                        first_page_contents
                    ]
                )
            )
        ]
    )
    container = Container(
        width = 400 , height = 750 , bgcolor = BG,
        border_radius = 38,
        content = Stack(
            controls = [
                page_1,
                page_2
            ]
        )
        
    )
    page.add(container)

app(target = main)
