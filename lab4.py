def paski(w, h, dzielnik):
    draw = False
    t = (h, w)
    tab = np.full(t, 255, dtype=np.uint8)
    thickness = int(w / dzielnik)
    number = int(w / thickness)
    dfrnce = int(255 / number)
    hue = 0 - dfrnce
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            if j % thickness == 0:
                draw = not draw
                hue += dfrnce
            if draw:
                tab[i, j] = hue
        hue = 0 - dfrnce
    return tab


T_szary = np.array(paski(1200, 900, 10))
img_g = Image.fromarray(T_szary)
img_g.save("fig2.png")
img_g.show()

ima1 = Image.merge('RGB', (img_g, g, b))
ima1.show()
ima2 = Image.merge('RGB', (r, img_g, b))
ima2.show()
ima3 = Image.merge('RGB', (r, g, img_g))

plt.figure(figsize=(16, 16))
for i in range(3):
    plt.subplot(2, 3, i + 1)
    plt.axis('off')
    plt.imshow(globals()[f'ima{i + 1}'])
plt.show()
