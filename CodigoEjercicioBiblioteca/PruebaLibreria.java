public class PruebaLibreria {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("Javier Muñoz Parra", "67381289021M");
        Cliente cliente2 = new Cliente("Paco Perez", "67381289021M");
        Libro libro = new Libro("Historia Porsche", "34722");
        

        System.out.println("=== Prestamo ===");
        cliente.solicitarLibro(libro); //El cliente solicita el libro
        System.out.println("Estado del libro: " + libro.getEstado());

        System.out.println(" ");

        System.out.println("== Solicitar Prestamo ==");
        Prestamo prestamo = new Prestamo(cliente, "16/03/2026", "23/03/2026");
        prestamo.crearPrestamo(libro);

        Prestamo prestamo2 = new Prestamo(cliente2,"18/03/2026", "28/03/2026");

        prestamo2.crearPrestamo(libro);

        System.out.println(" ");

        System.out.println("=== Devolver Libro ===");
        prestamo.registrarDevolucion("Historia Porsche", "16/03/2026");
        System.out.println("Estado del libro devuelto a: " + libro.getEstado());


    }   
    
}
