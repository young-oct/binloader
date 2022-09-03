# -*- coding: utf-8 -*-
# @Time    : 2022-09-03 16:33
# @Author  : young wang
# @FileName: bin2arr.py
# @Software: PyCharm

import numpy as np
from OssiviewBufferReader import OssiviewBufferReader

if __name__ == '__main__':
    file = '../data/nail.bin'

    reader = OssiviewBufferReader(file)
    data = np.array(reader.data["DAQ Buffer"], dtype='float64')
    #
    div = reader.header.metaData['Header']['Meta Data']['DIV']
    div = np.array(div)
    div = div[div < data.shape[3]]

    clean = np.zeros([data.shape[0], data.shape[2], data.shape[3] - len(div)], dtype=data.dtype)

    for g in range(data.shape[0]):
        for i in range(0, data.shape[2]):
            k = 0
            for j in range(data.shape[3]):
                if j not in div:
                    clean[g, i, k] = data[g, :, i, j]
                    k = k + 1

    raw = clean.reshape(-1, 1460)
    file_path ='../data/name.npz'
    np.savez(file_path, raw)
