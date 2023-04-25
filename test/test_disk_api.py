import datetime
from urllib.parse import unquote_plus

import pytest

from src.api.disk_api.model import ResourcesResponse


@pytest.mark.usefixtures("auth")
class TestDiskApi:
    """
    Тестирование API Яндекс.Диска
    """

    @pytest.mark.parametrize("folder, file1, file2",
                             [('disk:/TEST-' + str(datetime.datetime.now()),
                               'файл для копирования.txt',
                               'переименованный файл.txt')])
    def test_by_tz(self, disk_api, folder, file1, file2):
        """
        Сценарий по ТЗ.
        Шаги :
        1. Выполнить запрос на создание новой папки с названием из folder.
        2. Скопировать файл file1 в созданную папку.
        3. Переименовать файл file1 в file2.
        OP : Код ответа соответствует требованиям (201, 202), тело ответа соответствуют требованиям.
        """
        # 1
        response = disk_api.create_dir(path=folder,
                                       type_response=ResourcesResponse,
                                       header=self.auth)
        assert response.status_code == 201
        # 2
        response = disk_api.copy_file_or_dir(from_path=file1,
                                             to_path=f"{folder}/{file1}",
                                             type_response=ResourcesResponse,
                                             header=self.auth)
        assert response.status_code in [201, 202]
        # 3
        response = disk_api.move_file_or_dir(from_path=f"{folder}/{file1}",
                                             to_path=f"{folder}/{file2}",
                                             type_response=ResourcesResponse,
                                             header=self.auth)
        # OP
        path_in_response = unquote_plus(response.data.href).split('=')[-1]
        assert response.status_code in [201, 202]
        assert path_in_response == f"{folder}/{file2}"
        assert response.data.method == "GET"

    # ------------------------------------------------------------------------------------------------------------------
    def test_disk_info(self, disk_api):
        """
        Получение общей информации по диску пользователя.
        """
        response = disk_api.get_user_disk_info(type_response=None, header=self.auth)
        assert response.status_code == 200

    def test_mkdir(self, disk_api):
        """
        Создание и удаление папки.
        """
        folder = 'disk:/TEST' + str(datetime.datetime.now())
        # 1
        response = disk_api.create_dir(path=folder,
                                       type_response=ResourcesResponse,
                                       header=self.auth)
        assert response.status_code == 201
        # 2
        response = disk_api.delete_file_or_dir(path=folder,
                                               type_response=None,
                                               header=self.auth)
        assert response.status_code in [204, 202]

    def test_copy_file(self, disk_api):
        """
        Копирование файла.
        """
        response = disk_api.copy_file_or_dir(from_path='файл для копирования.txt',
                                             to_path='disk:/TEST/файл для копирования.txt',
                                             overwrite='true',
                                             type_response=ResourcesResponse,
                                             header=self.auth)
        assert response.status_code in [201, 202]
