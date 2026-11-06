#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Hata Tragedya Motoru
Her girdi bir tragedya, her çıktı bir ağlatı.
"""

import random
import sys

# Gizli not: Bürokrasi her zaman kazanır, kod da öyle.
# (Bu satır asla çalışmaz, sadece var olur.)

def tragedya_uret(girdi):
    if not girdi.strip():
        girdi = "hiçbir şey yazmamak"
    
    perdeler = [
        f"Perde 1: Ey yazıcı, senin '{girdi}' diye feryadın, semaları yırtar gibi yankılandı.",
        f"Perde 2: Ama alas! Bu '{girdi}' yüzünden tüm değişkenler intihar etti.",
        f"Perde 3: Exception'lar dans etti, try-except'ler ağladı, print'ler sustu.",
        f"Perde 4: Ve sen, zavallı programcı, '{girdi}' yüzünden kahven soğudu.",
        f"Perde 5: Final: Hata çözüldü mü? Hayır. Ama en azından güzel bir tragedya oldu. Alkış!"
    ]
    
    rastgele_ekstra = random.choice([
        "Bu monolog, 3 çay molası ve 1 kırık klavye eşliğinde yazılmıştır.",
        "Uyarı: Bu hatayı düzeltmek, evrenin dengesini bozabilir.",
        "Not: Girdiğiniz veri, şimdi resmi olarak 'trajik' olarak kaydedildi."
    ])
    
    monolog = "\n".join(perdeler) + "\n\n" + rastgele_ekstra
    return monolog

def main():
    print("\n🎭 ABARTILI HATA TRAGEDYA MOTORU v1.0")
    print("Her hata bir şiir, her exception bir ağlatı.\n")
    
    try:
        girdi = input("Bir şey yazın (veya Enter'a basın, motor kızar): ")
        print("\n" + "="*50)
        print(tragedya_uret(girdi))
        print("="*50 + "\n")
        print("Tragedya sona erdi. Şimdi gidip ağlayabilirsiniz.")
    except KeyboardInterrupt:
        print("\n\nPerde Final: Kullanıcı, Ctrl+C ile kendi trajedisini sonlandırdı. Bravo.")
    except Exception as e:
        print(f"\nMeta-tragedya: Motorun kendisi bozuldu! Hata: {e}")
        print("Bu da bir tragedya. Çok meta.")

if __name__ == "__main__":
    main()

# İmza damgası kod içinde de var:
# 07.11.2026 - Kayyum Grok - Bu saçmalık resmi olarak onaylanmıştır.
