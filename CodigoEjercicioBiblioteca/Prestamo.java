public class Prestamo {
    //Atributos de la clase
    private String fechaInicioPrestamo;
    private Libro libro;
    private Cliente cliente;
    private String fechaFinPrestamo;

    //metodo constructor
    public Prestamo(Cliente cliente, Libro libro, String fechaInicioPrestamo, String fechaFinPrestamo){
        this.cliente = cliente;
        this.libro = libro;
        this.fechaInicioPrestamo = fechaInicioPrestamo;
        this.fechaFinPrestamo = fechaInicioPrestamo;
        libro.actualizarEstado("Prestado");
    }

    public String getFechaInicioPrestamo() {
        return fechaInicioPrestamo;
    }

    public void setFechaInicioPrestamo(String fechaInicioPrestamo) {
        this.fechaInicioPrestamo = fechaInicioPrestamo;
    }

    public void setFechaFinPrestamo(String fechaFinPrestamo) {
        this.fechaFinPrestamo = fechaFinPrestamo;
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
