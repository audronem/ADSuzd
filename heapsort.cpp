#include <iostream>

using namespace std;

void heapify(int a[], int n, int i){
    int didziausias=i;
    int kaire=2*i+1;
    int desine=2*i+2;

    if(kaire<n&&a[kaire]>a[didziausias]){
        didziausias=kaire;
    }
    if(desine<n&&a[desine]>a[didziausias]){
        didziausias=desine;
    }
    if(didziausias!=i){
        swap(a[i], a[didziausias]);
        heapify(a, n, didziausias);
    }
}

void heapsort(int a[], int n){
    for(int i=n/2-1; i>=0; i--){
        heapify(a, n, i);
    }
    for(int i=n-1; i>=0; i--){
        swap(a[0], a[i]);
        heapify(a, i, 0);
    }
}

int main(){
    int a[]={1, 17, 10, 5, 3, 20, 4};
    int n=sizeof(a)/sizeof(a[0]);
    heapsort(a, n);
    for(int i=0; i<n; i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
