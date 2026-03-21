import ipaddress

# Se define la IP del ejercicio
red_principal = ipaddress.IPv4Network('192.15.15.0/24')

# Generamos las subredes con el nuevo prefijo /18
subredes = list(red_principal.subnets(new_prefix=29))[:30]

with open('tabla_latex.tex', mode='w', encoding='utf-8') as archivo:
    # Encabezado de la tabla para multiples páginas (longtable)
    archivo.write(r"\begin{center}" + "\n")
    archivo.write(r"\begin{longtable}{|c|c|c|c|c|}" + "\n")
    archivo.write(r"\hline" + "\n")
    archivo.write(r"\textbf{Subred} & \textbf{Dirección de Red} & \textbf{Primera IP Útil} & \textbf{Última IP Útil} & \textbf{Broadcast} \\ \hline" + "\n")
    archivo.write(r"\endfirsthead" + "\n\n")
    
    # Encabezado para las páginas secundarias
    archivo.write(r"\multicolumn{5}{c}%" + "\n")
    archivo.write(r"{{\bfseries Continuación de la página anterior...}} \\" + "\n")
    archivo.write(r"\hline" + "\n")
    archivo.write(r"\textbf{Subred} & \textbf{Dirección de Red} & \textbf{Primera IP Útil} & \textbf{Última IP Útil} & \textbf{Broadcast} \\ \hline" + "\n")
    archivo.write(r"\endhead" + "\n\n")
    
    # Pie de página cuando la tabla se corta
    archivo.write(r"\hline \multicolumn{5}{|r|}{{Continúa en la siguiente página...}} \\ \hline" + "\n")
    archivo.write(r"\endfoot" + "\n\n")
    
    # Pie de página final de la tabla
    archivo.write(r"\hline" + "\n")
    archivo.write(r"\endlastfoot" + "\n\n")
    
    # Generación automatizada de las 720 filas
    for i, subred in enumerate(subredes, 1):
        red = str(subred.network_address)
        primera = str(subred.network_address + 1)
        ultima = str(subred.broadcast_address - 1)
        broadcast = str(subred.broadcast_address)
        
        # Formato exacto de fila en LaTeX
        archivo.write(f"        {i} & {red} & {primera} & {ultima} & {broadcast} \\\\ \\hline\n")

    archivo.write(r"\end{longtable}" + "\n")
    archivo.write(r"\end{center}" + "\n")

print("Archivo tabla_latex.tex generado exitosamente.")