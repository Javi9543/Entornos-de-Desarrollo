public class Libro {
    //Atributos de la clase
    private String nombre;
    private int numLibro;
    private String estado;

    //metodo constructor
    public Libro(String nombLibro, int numLibro){
        this.nombre = nombLibro;
        this.numLibro = numLibro;
        estado = "Disponible";
    }
    
    //metodos de la clase
    public void actualizarEstado(String nuevoEstado){
        this.estado = nuevoEstado;
        System.out.println("El libro" + nombre + ", esta: " + estado);
    }

    //metodos get y set
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getNumLibro() {
        return numLibro;
    }

    public void setNumLibro(int numLibro) {
        this.numLibro = numLibro;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    
    
}
