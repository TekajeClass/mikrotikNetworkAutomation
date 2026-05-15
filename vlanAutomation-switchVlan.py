import paramiko
import time

def configure_mikrotik(host, username, password, commands, device_name):
    print(f"\n[{device_name}] Memulai koneksi ke {host}...")
    
    # Inisialisasi SSH Client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Melakukan koneksi SSH
        client.connect(hostname=host, username=username, password=password, timeout=10)
        print(f"[{device_name}] Berhasil terhubung!")
        
        # Eksekusi perintah satu per satu
        for cmd in commands:
            print(f"  -> Eksekusi: {cmd}")
            stdin, stdout, stderr = client.exec_command(cmd)
            
            # Beri jeda sedikit agar RouterOS selesai memproses command sebelumnya
            time.sleep(0.5)
            
            # Tangkap jika ada pesan error dari CLI
            error_msg = stderr.read().decode().strip()
            if error_msg:
                print(f"     [!] Error: {error_msg}")
                
        print(f"[{device_name}] Konfigurasi selesai!\n")
        
    except paramiko.AuthenticationException:
        print(f"[{device_name}] Autentikasi gagal. Cek username/password.")
    except Exception as e:
        print(f"[{device_name}] Gagal terhubung atau terjadi error: {e}")
    finally:
        client.close()


# ==========================================
# 1. KONFIGURASI SWITCH VLAN
# ==========================================
switch_ip = "100.100.10.2"                    # UBAH DENGAN IP BACKBONE MIKROTIK
switch_user = "admin"
switch_pass = ""

switch_commands = [
    "/system identity set name=SW-Vlan",
    
    # Bridge
    "/interface bridge add name=bridge-vlan protocol-mode=rstp",
    "/interface bridge port add bridge=bridge-vlan interface=ether1",
    "/interface bridge port add bridge=bridge-vlan interface=ether2",
    "/interface bridge port add bridge=bridge-vlan interface=ether3",
    
    # Switch Ingress Translation (Access Ports)
    "/interface ethernet switch ingress-vlan-translation add ports=ether2 customer-vid=0 new-customer-vid=2",
    "/interface ethernet switch ingress-vlan-translation add ports=ether3 customer-vid=0 new-customer-vid=3",
    
    # Switch Egress Tag (Trunk Ports)
    "/interface ethernet switch egress-vlan-tag add vlan-id=2 tagged-port=ether1",
    "/interface ethernet switch egress-vlan-tag add vlan-id=3 tagged-port=ether1",
    "/interface ethernet switch egress-vlan-tag add vlan-id=99 tagged-port=ether1,switch1-cpu",
    
    # Switch VLAN Table
    "/interface ethernet switch vlan add vlan-id=2 ports=ether1,ether2",
    "/interface ethernet switch vlan add vlan-id=3 ports=ether1,ether3",
    "/interface ethernet switch vlan add vlan-id=99 ports=ether1,switch1-cpu"
]

# Eksekusi Automasi
if __name__ == "__main__":

    # Pastikan PC yang menjalankan script ini bisa mengakses ip address switch
    # agar bisa mengkonfigurasi Switch
    configure_mikrotik(switch_ip, switch_user, switch_pass, switch_commands, "SWITCH-VLAN")
    
    print("[*] Seluruh proses automasi telah selesai di-deploy.")