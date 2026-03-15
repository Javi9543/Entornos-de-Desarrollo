public class Cliente {
    //Atributos
    private String nombre;
    private String dni;

    //metodo constructor
    public Cliente(String nom, String dni){
        this.dni = dni;
        this.nombre = nom;
    }

    //metodos de la clase

    public void solicitarLibro(Libro nombLibro, Bibliotecario bibliotecario){
        if (nombLibro.getEstado().equals("Disponible")) {
            bibliotecario.crearPrestamo(this, nombLibro); //pongo this, para que el programa sepa QUIEN, esta solicitando el prestamo del libro
        } else {
            System.out.println("El libro" + nombLibro + ", No esta disponible, intente solicitar otro libro");
        }
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
