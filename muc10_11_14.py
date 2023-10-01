def so_sv_dat_tung_loai_diem():
    # Lấy điểm từ cột tương ứng
    diemAp = in_data[:, 5]
    diemA = in_data[:, 6]
    diemBp = in_data[:, 7]
    diemB = in_data[:, 8]
    diemCp = in_data[:, 9]
    diemC = in_data[:, 10]
    diemD = in_data[:, 11]
    diemDp = in_data[:, 12]
    diemF = in_data[:, 13]

    # Tính tổng số sinh viên trong lớp
    tongsv = in_data[:, 1].sum()

    # Tính số lượng sinh viên đạt từng loại điểm
    so_sv_A = np.sum(diemA == 'A')
    so_sv_Bc = np.sum(diemBc == 'B+')
    so_sv_Cp = np.sum(diemCp == 'C+')
    so_sv_C = np.sum(diemC == 'C')
    so_sv_D = np.sum(diemD == 'D')
    so_sv_Dp = np.sum(diemDp == 'D+')
    so_sv_F = np.sum(diemF == 'F')

    # Tính phần trăm điểm cho từng loại điểm
    phan_tram_A = (so_sv_A / tongsv) * 100
    phan_tram_Bc = (so_sv_Bc / tongsv) * 100
    phan_tram_Cp = (so_sv_Cp / tongsv) * 100
    phan_tram_C = (so_sv_C / tongsv) * 100
    phan_tram_D = (so_sv_D / tongsv) * 100
    phan_tram_Dp = (so_sv_Dp / tongsv) * 100
    phan_tram_F = (so_sv_F / tongsv) * 100

    print(f'Phần trăm sinh viên đạt điểm A+: {phan_tram_A:.2f}%')
    print(f'Phần trăm sinh viên đạt điểm A: {phan_tram_A:.2f}%')
    print(f'Phần trăm sinh viên đạt điểm B+: {phan_tram_Bc:.2f}%')
    print(f'Phần trăm sinh viên đạt điểm C+: {phan_tram_Cp:.2f}%')
    print(f'Phần trăm sinh viên đạt điểm C: {phan_tram_C:.2f}%')
    print(f'Phần trăm sinh viên đạt điểm D: {phan_tram_D:.2f}%')
    print(f'Phần trăm sinh viên đạt điểm D+: {phan_tram_Dp:.2f}%')
    print(f'Phần trăm sinh viên đạt điểm F: {phan_tram_F:.2f}%')