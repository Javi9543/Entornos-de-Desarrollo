public class Prestamo {
    private String iniPrestamo;
    private String finPrestamo;
    private Libro libro;
    private Cliente cliente;

    public Prestamo(Cliente cliente, String iniPrest, String finPrestamo){
        this.cliente = cliente;
        this.iniPrestamo = iniPrest;
        this.finPrestamo = finPrestamo;
    }

    public void crearPrestamo(Libro libro){
        this.libro = libro;
        if ("Disponible".equals(libro.getEstado())) {
            libro.setEstado("Prestado");
            System.out.println("Tienes para devolverlo desde: " + iniPrestamo + " hasta " + finPrestamo);
        } else if ("Prestado".equals(libro.getEstado())) {
            System.out.println( cliente.getNombre() + ", El libro solicitado, está prestado o no esta en la biblioteca");
        }
    }

    public void registrarDevolucion(String nombre, String fechadev){
        if (nombre.equals(libro.getNombreLibro())) {
            libro.setEstado("Disponible");
            this.finPrestamo = fechadev;
            System.out.println(libro.getNombreLibro() + ", Libro devuelto por, " + cliente.getNombre());
        } else {
            System.out.println(cliente. getNombre() + ", El libro a devolver no es nuestro");
        }
    }

    public String getIniPrestamo() {
        return iniPrestamo;
    }

    public void setIniPrestamo(String iniPrestamo) {
        this.iniPrestamo = iniPrestamo;
    }

    public String getFinPrestamo() {
        return finPrestamo;
    }

    public void setFinPrestamo(String finPrestamo) {
        this.finPrestamo = finPrestamo;
    }

    public Libro getLibro() {
        return libro;
    }

    public void setLibro(Libro libro) {
        this.libro = libro;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    
}
