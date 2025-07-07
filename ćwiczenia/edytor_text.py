import edytor as e

text = e.Text("Hello World")
bold_text = e.Bold(text)
bold_italic_text = e.Bold(e.Italic(e.UnderLine(text)))
dif_order = e.UnderLine(e.Bold(e.Italic(text)))

print("Zwykły tekst: ", text.render())
print("Pogrubiony: ", bold_text.render())
print(bold_italic_text.render())
print(dif_order.render())
