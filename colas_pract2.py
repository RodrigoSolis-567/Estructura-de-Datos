class Order:
    def __init__(self, qtty: int, customer: str):
        self.customer = customer
        self.qtty = qtty
    def print(self):
        print(f"    Customer: {self.getCustomer()}")
        print(f"    Quantity: {self.getQtty()}")
        print("    -------------------")

    def getQtty(self) -> int:
        return self.qtty

    def getCustomer(self) -> str:
        return self.customer


class Node:
    def __init__(self, info, next=None):
        self.info = info   
        self.next = next  
    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def isEmpty(self) -> bool:
        return self._size == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.front_node.getInfo()
    
    def enqueue(self, info):
        new_node = Node(info)
        if self.isEmpty():
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.setNext(new_node)
            self.rear_node = new_node
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        info = self.front_node.getInfo()
        self.front_node = self.front_node.getNext()
        self._size -= 1
        if self.isEmpty():
            self.rear_node = None
        return info

    # Método printInfo
    def printInfo(self):
        print("********** QUEUE DUMP **********")
        print(f"    Size: {self.size()}")
        node = self.front_node
        idx = 1

        while node is not None:
            print(f"    ** Element {idx}")
            order = node.getInfo()
            if hasattr(order, 'print'):
                order.print()
            else:
                print(f"    {order}")
            node = node.getNext()
            idx += 1
        print("********************************\n")


class TestQueue:
    @staticmethod
    #metodo main
    def main():
        queue = Queue()
        
        print("=== Recorrido de la cola ===")
        order1 = Order(20, "cust1")
        queue.enqueue(order1)
        queue.printInfo()

        order2 = Order(30, "cust2")
        queue.enqueue(order2)
        queue.printInfo()

        order3 = Order(40, "cust3")
        queue.enqueue(order3)
        queue.printInfo()

        order4 = Order(50, "cust3")
        queue.enqueue(order4)
        queue.printInfo()

        # Probar  método front
        print("\n=== Test método front() ===")
        f_elem = queue.front()
        if f_elem:
            print(f"Siguiente pedido al frente: Cliente = {f_elem.getCustomer()}, Cantidad = {f_elem.getQtty()}")

        # Probar metodo dequeue
        print("\n=== Test método dequeue() ===")
        dequeued_order = queue.dequeue()
        if dequeued_order:
            print(f"Pedido atendido/extraído de: {dequeued_order.getCustomer()}")
        queue.printInfo()

        dequeued_order = queue.dequeue()
        if dequeued_order:
            print(f"Pedido atendido/extraído de: {dequeued_order.getCustomer()}")
        queue.printInfo()


if __name__ == "__main__":
    TestQueue.main()
