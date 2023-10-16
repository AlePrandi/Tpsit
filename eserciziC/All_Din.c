// Si usa la malloc per l'allocazione dinamica
// m -> memory  alloc -> allocation
// ritorna sempre un puntatore a void, quindi si fa il casting

int main()
{
    int *p;
    p = (int *) malloc (5 * sizeof(int)); // spazio in memoria dell'array   (int *) -> casting
    // 5 n_celle sizeof -> spazio occupato dal tipo di variabile
}