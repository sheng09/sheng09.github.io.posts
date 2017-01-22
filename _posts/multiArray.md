---
title: Multidimensional Array in C/C++
date: 2017-01-22 21:37:45
categories: Programming
tags: [c++]
---

This post introduce methods of constructing and calling multidimensional array in C/C++.

<!--more-->

<!--toc-->

The key point of mutlidimensional array is using the pointer to pointers. For example, constructing two dimensional array requires a pointer array, each element of which points to an one dimensional array. 


------------------

## C
A simple method is:
### A simple method
``` c
int** alloc_float2(int nx, int ny) {
    float **px  = (float **) malloc (nx*sizeof(float**));
    float *pdat = (float  *) malloc (nx*ny*sizeof(float));
    for(int ix = 0; ix < nx; ++ix)
        px[ix] = pdat + ix * ny;
    return px;
}
void free_float2(float **p){
    free(p[0]); free(p);
}

//usage
float **m2 = alloc_float2(4,5);
// calling to m2[i][j];
//...
free_float2(m2);
```
However, this is a bad design since both malloc and free are called for twice. More over, forgetting to free the data scope (`p[0]`) often happens.

### Better method
A better method is put the pointer array and data scope array together. Thus, operations of malloc and free are called for only once.

``` c
int** alloc_f2(int nx, int ny){
    float **ptr  = (float**) malloc (nx * sizeof(float*) + nx*ny*sizeof(float));
    float  *pdat = (float*) (ptr + nx);
    for(int ix = 0; ix < nx; ++ix)
        ptr[ix] = pdat + ix * ny;
    return ptr;
}

//usage
float **m2 = alloc_f2(10,10);
// calling m2[i][j];
free(m2); //
```


------------------

## C++
It is disaster for constructing multi-dimensional array in C because of lots of types, such as `int`, `float`, `double`... We need to write codes repeatedly for these types. However, C++ provides a nice method for simplify these, TEMPLATE!

``` c++
template <class T>
T** alloc2(std::size_t nx, std::size_t ny, T*** p_m2 ) {
    *p_m2 = (T**) ( new char [sizeof(T)*nx*ny + sizeof(T*)*nx] );
    T* pdat = *p_m2 + nx;
    for(std::size_t ix = 0; ix < nx; ++ix)
        (*p_m2)[ix] = pdat + ix * ny;
    return *p_m2;
}

// usage
float **m;
alloc2(3,4,&m);
// call m[i][j];
delete m;
```

## Elegant method
C++ provides `class` for us to packaging everything. Why not using it?

``` c++
template <class T>
class MAT2{
public:
    MAT2(std::size_t nx, std::size_t ny) : d_nx(nx), d_ny(ny) { dat = new T [nx*ny]; }
    ~MAT2() {delete dat; }
    T* operator[](std::size_t ix) { return (T+ix*ny); }
private:
    std::size_t d_nx, d_ny;
    T* dat;
};

//usage
MAT2<double> m(4,5);
//...
```

Example above is the simplest design for two dimensional array. More advanced design is [gsw](https://github.com/sheng09/sheng09.github.io.posts/_posts/multiArray).





