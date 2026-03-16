public class PruebaLibreria {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("Javier Muñoz Parra", "67381289021M");
        Libro libro = new Libro("Historia Porsche", 34722);
        Bibliotecario bibliotecario = new Bibliotecario(138921, "Paquito Fernandez");

        System.out.println("=== Prestamo ===");
        cliente.solicitarLibro(libro, bibliotecario, "15/03/2026", "20/03/2026"); //El cliente solicita el libro
        System.out.println("Estado del libro: " + libro.getEstado());

        System.out.println(" ");

        System.out.println("=== Devolver Libro ===");
        bibliotecario.registrarDevolucion(libro);
        System.out.println("Estado del libro: " + libro.getEstado());


    }   
    
}
