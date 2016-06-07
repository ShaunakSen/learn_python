while True:
    try:
        number =  int(input('Enter fav no: \n'))
        print(10/number)
        break
    except ValueError:
        print('Make sure u enter a no \n')

    except ZeroDivisionError:
        print('Dont pick 0 \n')

    except:
        break

    finally:
        print('Executes no matter what \n')


