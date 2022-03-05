# LATIHAN4DPBO2022

Repository ini berisikan Latihan 4 pada mata kuliah Desain Pemrograman Berorientasi Objek tahun 2022.

> Saya Ghifari Octaverin (2000952) mengerjakan tugas LATIHAN4DPBO2022 dalam mata kuliah Desain dan Pemrograman Berbasis Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

### Modul

Modul dari latihan ini dapat di akses melalui [Modul 4 - Multiple & Hierarchical Inheritance](https://docs.google.com/document/d/1zSLOCPvmSSnlj8vAcLW6R4KRVh9lF7K2SYfrjp04Wqc/edit)

### Bahasa

Dalam project kali ini hanya menggunakan satu bahasa pemrograman saja, yaitu Python.

### Desain Project dan Penjelasan Project

<p align="center">
  <img src="https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Desain%20Tugas%204.png" alt="Desain Latihan 4"/>
</p>

- Kelas Vehicle menjadi parent dari kelas Airplane dan kelas Ship. Hal tersebut dikarenakan Airplane dan Ship merupakan salah satu dari jenis Vehicle sehingga mereka merupakan child dari kelas Vehicle. Karena itu, hubungan ini cocok menggunakan Hierarchical Inheritance.
- Pada kelas Vehicle saya menambahkan atribut 'velocity', yang saya rasa cocok untuk ditambahkan karena setiap jenis Vehicle memiliki kecepatan tempuhnya masing-masing.
- Kelas Driver merupakan child dari kelas Person dan kelas Job. Hal tersebut dikarenakan kelas Driver memiliki sifat-sifat yang sama dengan kelas parentnya. Kelas Driver merupakan kelas yang melibatkan Person dan Job, dimana Driver adalah manusia (Person) dan sebuah pekerjaan (Job). Kelas Person lebih dominan terhadap kelas Job, hal ini dikarenakan pada kelas Person memiliki sifat yang penting didalam kelas Driver. Berdasarkan alasan-alasan tersebut, saya rasa Multiple Inheritance cocok untuk menggambarkan hubungan ini.
- Pada kelas Person memiliki atribut isMale yang bertipe boolean. Sehingga bisa diisi dengan True untuk laki-laki (male) dan False untuk perempuan (female).

### Cara Eksekusi Kode Program

Adapun cara mengeksekusi kode program dalam Repository ini adalah sebagai berikut.

```
py (nama file).py
```

### Hasil dari Kode Program Setelah Dijalankan

- ### Airplane Class
  ![Latihan 4 Airplane Class](https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Screenshot/Latihan4_AirplaneClass.png)
- ### Ship Class
  ![Latihan 4 Ship Class](https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Screenshot/Latihan4_ShipClass.png)
- ### Vehicle Class
  ![Latihan 4 Vehicle Class 1](https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Screenshot/Latihan4_VehicleClass1.png)
  ![Latihan 4 Vehicle Class 2](https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Screenshot/Latihan4_VehicleClass2.png)
- ### Driver Class
  ![Latihan 4 Driver Class](https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Screenshot/Latihan4_DriverClass.png)
- ### Person Class
  ![Latihan 4 Person Class](https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Screenshot/Latihan4_PersonClass.png)
- ### Job Class
  ![Latihan 4 Job Class](https://github.com/ghifari21/LATIHAN4DPBO2022/blob/8d25e49bb9cedc7a6d33d4eacfb11311ba88b722/Screenshot/Latihan4_JobClass.png)

## Thankyou