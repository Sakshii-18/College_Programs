signal = input("Enter Signal: Red / Green / Yellow: ").lower()

match signal :
    case 'red' :
        print("Stop")
    case 'yellow' :
        print("Get Ready")
    case 'green' :
        print("Go")
    case _:
        print("Invalid Signal")