public class Cliente {
    //Atributos de la clase
    private String nombre;
    private String dni;
    private Libro libro;

    public Cliente(String nomb, String dni){
        this.nombre = nomb;
        this.dni = dni;
    }

    public void solicitarLibro(Libro libro){
        System.out.println("El cliente " + nombre + "Pide el libro" + libro.getNombreLibro());
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

}
