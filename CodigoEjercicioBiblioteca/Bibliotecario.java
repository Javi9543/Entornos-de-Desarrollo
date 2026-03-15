public class Bibliotecario {
    //Atributos de la clase
    private int idBibliotecario;
    private String nomBibliotecario;

    //metodo constructor
    
    public Bibliotecario(int idBib, String nombre) {
        this.nomBibliotecario = nombre;
        this.idBibliotecario = idBib;        
    }

    //metodos de la clase
    public void crearPrestamo(Cliente cliente, Libro libro, String fini, String fFin){
        new Prestamo(cliente, libro, fini, fFin);
        System.out.println("Prestamo realizado, desde " + fini + " hasta " + fFin);
    }

    public void registrarDevolucion(Libro libro){
        libro.actualizarEstado("Disponible");
        System.out.println("Devolucion Registrada correctamente");
    }

    //metodos get y set
    public int getIdBibliotecario() {
        return idBibliotecario;
    }

    public void setIdBibliotecario(int idBibliotecario) {
        this.idBibliotecario = idBibliotecario;
    }

    public String getNomBibliotecario() {
        return nomBibliotecario;
    }

    public void setNomBibliotecario(String nomBibliotecario) {
        this.nomBibliotecario = nomBibliotecario;
    }

    
}
