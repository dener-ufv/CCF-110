speed = float(input("velocidade média: "))
time = float(input("tempo: "))
print("foram percorridos {0} Km".format(time*speed))
print("foram gastos {:.3f} L".format(time*speed/12))