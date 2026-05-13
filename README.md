# Mikrotik Network Automation

Repository ini berisi skrip Python untuk otomatisasi konfigurasi VLAN dan layanan DHCP/NAT pada perangkat MikroTik RouterOS.

## Isi Folder

- `vlanAutomation.py`
  - Konfigurasi otomatisasi untuk perangkat `Router-CORE` saja.
  - Menambahkan VLAN, alamat IP, DHCP pool, DHCP server, jaringan DHCP, dan NAT masquerade.

- `vlanAutomation-routerCore.py`
  - Konfigurasi `Router-CORE` dan `SWITCH-VLAN` secara bersamaan.
  - Mengotomasi konfigurasi router core dan switch VLAN melalui SSH.

- `vlanAutomation-switchVlan.py`
  - Konfigurasi khusus untuk `SWITCH-VLAN`.
  - Menyiapkan bridge, port bridge, ingress translation, egress VLAN tagging, dan tabel VLAN switch.

- `perintahMikrotik.txt`
  - Catatan perintah MikroTik yang dibuat sebagai panduan konfigurasi manual.

## Persyaratan

- Python 3.x
- Paket `paramiko`

Instalasi paket:

```bash
pip install paramiko
```

## Cara Pakai

1. Buka masing-masing skrip Python, lalu sesuaikan alamat IP, username, dan password MikroTik.
2. Pastikan perangkat target dapat diakses dari mesin yang menjalankan skrip.
3. Jalankan skrip yang diinginkan:

```bash
python vlanAutomation.py
python vlanAutomation-routerCore.py
python vlanAutomation-switchVlan.py
```

## Catatan Penting

- `vlanAutomation-routerCore.py` mencoba mengkonfigurasi router core dan switch VLAN dari satu skrip. Pastikan router dan switch dapat dijangkau.
- `vlanAutomation-switchVlan.py` hanya mengkonfigurasi switch VLAN.
- Semua skrip menggunakan SSH untuk mengeksekusi perintah MikroTik; pastikan SSH diaktifkan dan kredensial benar.
- Ubah nilai `router_ip`, `switch_ip`, `router_user`, `switch_user`, `router_pass`, dan `switch_pass` sesuai lingkungan Anda.

## Peringatan

- Skrip ini mengeksekusi perintah konfigurasi langsung ke perangkat. Gunakan di lingkungan lab atau test terlebih dahulu.
- Jangan jalankan pada perangkat produksi tanpa verifikasi yang memadai.
