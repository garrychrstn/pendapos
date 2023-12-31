from django import forms
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

class SearchBalita(forms.Form):
    nama = forms.CharField(
        max_length=50,
        label = '',
        label_suffix= '',
        widget=forms.TextInput(attrs={
            'placeholder' : 'Nama'
        })
    )
class BulanForm(forms.Form):
    pilihanbulan = [
    ('Januari', 'Januari'),
    ('Februari', 'Februari'),
    ('Maret', 'Maret'),
    ('April', 'April'),
    ('Mei', 'Mei'),
    ('Juni', 'Juni'),
    ('Juli', 'Juli'),
    ('Agustus', 'Agustus'),
    ('September', 'September'),
    ('Oktober', 'Oktober'),
    ('November', 'November'),
    ('Desember', 'Desember'),
]
    bulan = forms.ChoiceField(
        widget = forms.Select,
        choices = pilihanbulan,
        label = 'Posyandu Bulan'

    )

class ProfilInput(forms.Form):
    nik = forms.IntegerField(
        label_suffix = ' ',
        label = ' ',
        widget=forms.TextInput(attrs={
            'placeholder' : 'NIK'
        })
    )
    nama = forms.CharField(
        max_length=30,
        label=' ', 
        label_suffix=' ',
        widget=forms.TextInput(attrs={
            'placeholder' : 'Nama Lengkap'
        })
    )
    namaibu = forms.CharField(
        max_length=30,
        label = '',
        label_suffix='',
        widget=forms.TextInput(attrs= {
            'placeholder' : 'Nama Ibu'
        })
    )
    nikibu = forms.IntegerField(
        required=True,
        label_suffix='',
        label = '',
        widget = forms.TextInput(attrs = {
            'placeholder' : 'NIK Ibu'
        })
    )
    pilihandusun = [
        ('Kerjo', 'Kerjo'),
        ('Sumberejo', 'Sumberejo'),
        ('Plandakan', 'Plandakan'),
        ('Kadipeso', 'Kadipeso'),
        ('Dumpul', 'Dumpul'),
        ('Derso', 'Derso')
    ]
    dusun = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class' : 'dusun'
        }),
        required = True,
        choices=pilihandusun,
        label = 'Dusun',
    )
    tgl = forms.DateField(
        label=' ', 
        label_suffix=' ',
        widget=forms.DateInput(attrs={
            'placeholder' : 'Tanggal Lahir',
            'class' : 'tgl',
            'type' : 'date'
        }))
    
    pilihankelamin = [
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan')
    ]
    kelamin = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = pilihankelamin,
        label = "Jenis Kelamin "
    )   

class PosyanduForm(forms.Form):
    pilihanbulan = [
    ('Januari', 'Januari'),
    ('Februari', 'Februari'),
    ('Maret', 'Maret'),
    ('April', 'April'),
    ('Mei', 'Mei'),
    ('Juni', 'Juni'),
    ('Juli', 'Juli'),
    ('Agustus', 'Agustus'),
    ('September', 'September'),
    ('Oktober', 'Oktober'),
    ('November', 'November'),
    ('Desember', 'Desember'),
]

    bulan = forms.ChoiceField(
        required = True,
        widget = forms.Select,
        choices = pilihanbulan,
        label = 'Posyandu Bulan'

    )
    bb = forms.IntegerField(
        required = True,
        label_suffix ='',
        label = '',
        widget = forms.TextInput(attrs = {
            'placeholder' : 'Berat Badan'
        })
    )
    tb = forms.IntegerField(
        required = True,
        label_suffix ='',
        label = '',
        widget = forms.TextInput(attrs = {
            'placeholder' : 'Tinggi Badan'
        })
    )
    ll = forms.IntegerField(
        required = True,
        label_suffix ='',
        label = '',
        widget = forms.TextInput(attrs = {
            'placeholder' : 'Lingkar Lengan'
        })
    )
    lk = forms.IntegerField(
        required = True,
        label_suffix ='',
        label = '',
        widget = forms.TextInput(attrs = {
            'placeholder' : 'Lingkar Kepala'
        })
    )
    ket = forms.CharField(
        required = False,
        label_suffix ='',
        label = '',
        widget = forms.TextInput(attrs = {
            'placeholder' : 'Keterangan'
        })
    )


