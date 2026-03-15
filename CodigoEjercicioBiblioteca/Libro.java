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
}
