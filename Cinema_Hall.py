class Star_Cinema:
    __hall_list = []

   
        
    def entry_hall(self):
       Star_Cinema.__hall_list.append(self)


class Hall(Star_Cinema):


 
    def __init__(self,rows,cols,hall_no) -> None:
        self.entry_hall()
        self.seats = {}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        

        
    def entry_show(self,id,movieName,Time):

        movieInfo =(id,movieName,Time)

        self.show_list.append(movieInfo)

        two_d_list = [[0,0,0,0,],
                      [0,0,0,0,],
                      [0,0,0,0,],
                      [0,0,0,0,]
                      ]

        self.seats.update({id:two_d_list})

    def book_seats(self,id,r,c):
        a  = self.seats.get(id)

        a[r][c]=1

        self.seats.update({id:a})

    def view_show_list(self):

        print(self.show_list)

    def view_available_seats(self,id):

        a= self.seats.get(id)

        for i in a:
            print(i)
            

myCinema = Hall(5,5,1)
myCinema.entry_show("1","JAWAN","2:10")
myCinema.entry_show("2","Aquaman","5:10")


while 1:
    print("Press 1 to view All the shows Running")

    print("Press 2 to view Available Seats and For ticket booking")
    print("Press 3 to Exit")
    a = input()
    print(a)
    if a =='1':
        myCinema.view_show_list()

    if a == '2':
        print("Enter the id for the Show u want to see Available Seats")
        ab = input()
        myCinema.view_available_seats(ab)
        print("Enter the id of the show and row and column of the seat u want to book")
        
        id = input()
        row = input()
        col = input()

        myCinema.book_seats(id,int(row),int(col))

    if a == '3':
        break   
        









    
    
 
    
