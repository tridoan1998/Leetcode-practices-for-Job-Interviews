//Tri Doan
//Section 4
//Problem 1
/*
An item has an integer ID, a price (in USD), and a Boolean flag called
 inStock that is true by default, but can be set to false when supplies of
  the item runout */

//A. [5 points] Implement the Item and PO (i.e. purchase order) classes.
class Item(val ID: Int, val price: Double, val inStock: Boolean = true) {
  //override all methods needed, (maybe)
  override def toString: String = ID + " " + price + " "+ inStock
  override def hashCode(): Int = super.hashCode()
  override def equals(obj: Any): Boolean = super.equals(obj)

  //getter
  def getID = ID
  def getprice= price
  def is_inStock = inStock

  //catch exception
  if (ID < 0 || price < 0) throw new IllegalArgumentException


}

object Item {
  def apply(ID: Int,  price: Double, inStock: Boolean = true) = new Item(ID, price, inStock)
}


//create PO class
class PO(val customber_number: Int, val items: Item) {
  //check if input is valid
  if (customber_number < 0) throw new IllegalArgumentException

  override def toString: String = customber_number + " " + items
  override def equals(obj: Any): Boolean = super.equals(obj)
  override def hashCode(): Int = super.hashCode()

}

//create instance
object PO {
  def apply( customber_number: Int, items: Item) = new PO( customber_number, items)

  def total(cusID: Int, po: List[PO]): Any = {
    val result = po.filter(_.items.ID != cusID).map(_.items.inStock)
    result
  }
}


//problem 3
//A. [10 Points] Complete the implementation of Warrior.
class Warrior(val name: String, private var health: Int = 100) {
  override def toString: String = name + "" + health

  if (health < 0) throw new IllegalArgumentException

  def attack(other: Warrior): Unit = {
    var randomDamage = scala.util.Random

    println( this.name + "is attacking" + other.name)
    this.health = this.health - 1
  }


  def compose2[T](list: List[T]) {}


  //blue.strategy = compose(List(spitFire, stomp, spitFire))
  def compose[T, S, U]( f: S=>U, g: T=>S): T=>U = {
    def r(x: T) = f(g(x))
    r _
  }

  def  strategy(): Unit =
  {

  }
  def doNothing(w: Warrior) = {}





}

object Warrior {
  def apply(name: String, health: Int) = new Warrior(name, health)
}


object midterm extends App{

  try {

    val orders = List(
      PO(0, Item(4, 12.95)),
      PO(2, Item(4, 12.95)),
      PO(0, Item(3, 2.75, false)),
      PO(1, Item(9, 8.25)),
      PO(1, Item(3, 12.95, false)),
      PO(2, Item(4, 2.75)),
      PO(0, Item(9, 8.25))
    )
    PO.total(0, orders)


    //problem 2

    def optionMap[T, S](mylist: List[T], stringToInt: String => Int): Any = {
      try {

        mylist.map(_.isInstanceOf[Int])
        for (i <- 0 to mylist.size) {
          if (mylist(i).isInstanceOf[Int]) {
            Some(mylist(i))
          }
          else throw new Exception
        }
      } catch {
        case e: Exception => None

      }

      println(optionMap(List("123", "456", "abc", "789"), (s: String) => s.toInt))

    }

    //problem 3
    val red = new Warrior("Red Sonya")
    val blue = new Warrior("Blue Velvet")
    red.strategy = Stomps
    blue.strategy = compose(List(spitFire, stomp, spitFire))

    def spitFire(opponent: Warrior) = {
      println("Spits fire")
      opponent.health -= 10
    }

    def stomp(opponent: Warrior) = {
      println("Stomps")
      opponent.health -= 7
    }
  }

  catch{
    case e: IllegalArgumentException => println(e)
  }
}

