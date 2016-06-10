# -*- coding: utf-8 -*-

import re

PARAM_RE = re.compile(r":param(?: (?P<type>\w+))? (?P<param>\w+): (?P<doc>.*)")
RTYPE_RE = re.compile(r":rtype: (?P<rtype>.*)")
TYPE_OF_RE = re.compile(r"^(?P<type1>\w+?) of (?P<type2>.+)$")


def get_params(docstring):
    result = []
    for m in PARAM_RE.finditer(docstring):
        result.append({
            "type": m.group("type"),
            "param": m.group("param"),
            "doc": m.group("doc"),
        })
    return result


def get_rtype(docstring):
    m = RTYPE_RE.search(docstring)
    if not m:
        return None
    return m.group("rtype")


def parse_type_of(s):
    m = TYPE_OF_RE.match(s)
    if not m:
        return s
    else:
        return (m.group("type1"), parse_type_of(m.group("type2")))
