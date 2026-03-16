public class Libro {
    //Atributos de la clase
    private String nombreLibro;
    private String numLibro;
    private String estado;

    public Libro(String nombre, String ISBN){
        this.nombreLibro = nombre;
        this.numLibro = ISBN;
        this.estado = "Disponible";
    }

    public String getNombreLibro() {
        return nombreLibro;
    }

    public void setNombreLibro(String nombreLibro) {
        this.nombreLibro = nombreLibro;
    }

    public String getNumLibro() {
        return numLibro;
    }

    public void setNumLibro(String numLibro) {
        this.numLibro = numLibro;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    
}
