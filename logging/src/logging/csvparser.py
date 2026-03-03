import csv
from typing import Dict, List, Union, cast


def _parser(
    file: str, header_opt: bool = False
) -> Union[List[str], List[Dict[str, str]]]:
    res = []

    with open(file, mode="r", encoding="utf-8") as f:
        lector = csv.reader(f)

        if header_opt:
            try:
                return next(lector)
            except StopIteration:
                return []

        for linea in lector:
            if len(linea) == 3:
                dict_log = {"fecha": linea[0], "nivel": linea[1], "mensaje": linea[2]}
                res.append(dict_log)
    return res


def csvinfo(ruta: str) -> List[Dict[str, str]]:
    # Get info from CSV file
    res = _parser(ruta, header_opt=False)
    return cast(List[Dict[str, str]], res)


def csvheaders(ruta: str) -> List[str]:
    # Get headers from CSV file
    res = _parser(ruta, header_opt=True)
    return cast(List[str], res)
