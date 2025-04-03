from linked_list import LinkedList

def main():
    ll = LinkedList()

    while True:
        print("\nMenú de Opciones:")
        print("1. Mostrar lista")
        print("2. Obtener longitud de la lista")
        print("3. Insertar al principio")
        print("4. Insertar al final")
        print("5. Insertar en una posición específica")
        print("6. Eliminar del principio")
        print("7. Eliminar del final")
        print("8. Eliminar en una posición específica")
        print("9. Buscar un valor en la lista")
        print("10. Salir")

        option = input("\nElige una opción (1-10): ")

        if option == "1":
            print("\nLista:", ll.display())

        elif option == "2":
            print("\nLongitud de la lista:", ll.list_length())

        elif option == "3":
            data = int(input("\nIngresa el valor a insertar al principio: "))
            ll.insert_at_beginning(data)
            print(f"\nValor {data} insertado al principio.")

        elif option == "4":
            data = int(input("\nIngresa el valor a insertar al final: "))
            ll.insert_at_end(data)
            print(f"\nValor {data} insertado al final.")

        elif option == "5":
            position = int(input("\nIngresa la posición para insertar: "))
            data = int(input("\nIngresa el valor a insertar: "))
            if ll.insert_at_position(position, data):
                print(f"\nValor {data} insertado en la posición {position}.")
            else:
                print("\nPosición inválida.")

        elif option == "6":
            data = ll.delete_from_beginning()
            if data is not None:
                print(f"\nValor {data} eliminado del principio.")
            else:
                print("\nLa lista está vacía.")

        elif option == "7":
            data = ll.delete_from_end()
            if data is not None:
                print(f"\nValor {data} eliminado del final.")
            else:
                print("\nLa lista está vacía.")

        elif option == "8":
            position = int(input("\nIngresa la posición para eliminar: "))
            data = ll.delete_from_position(position)
            if data is not None:
                print(f"\nValor {data} eliminado de la posición {position}.")
            else:
                print("\nPosición inválida o lista vacía.")

        elif option == "9":
            value = int(input("\nIngresa el valor a buscar: "))
            position = ll.search(value)
            if position != -1:
                print(f"\nEl valor {value} se encuentra en la posición {position}.")
            else:
                print(f"\nEl valor {value} no se encuentra en la lista.")

        elif option == "10":
            print("\nSaliendo...")
            break

        else:
            print("\nOpción no válida. Por favor, elige una opción entre 1 y 10.")

if __name__ == "__main__":
    main()
