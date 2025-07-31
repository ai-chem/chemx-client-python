# chemx_client/client.py

import requests
import pandas as pd
from typing import Optional, Dict, Any


class ChemXAPIError(Exception):
    pass


class ChemXClient:

    def __init__(self, base_url: str = "https://chemx-backend.onrender.com"):
        """
        base_url (str): Адрес запущенного сервера ChemX-backend.
        По умолчанию смотрит на публичный сервер на Render.
        """
        self.base_url = f"{base_url.rstrip('/')}/api/v1"
        self.session = requests.Session()

    def _get_and_parse(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:

        full_url = f"{self.base_url}/{endpoint}"

        # Параметры по умолчанию для запроса
        request_params = {"file_format": "json"}
        if params:
            request_params.update(params)

        try:
            response = self.session.get(full_url, params=request_params)
            response.raise_for_status()

            data = response.json()
            return pd.DataFrame(data)

        except requests.exceptions.HTTPError as e:
            raise ChemXAPIError(f"Ошибка от API ({e.response.status_code}) для {full_url}: {e.response.text}") from e
        except requests.exceptions.RequestException as e:
            raise ChemXAPIError(f"Ошибка сети или подключения к {full_url}: {e}") from e
        except ValueError as e:
            raise ChemXAPIError(f"Не удалось декодировать JSON от {full_url}: {e}") from e

    # --- Cytotox ---

    def get_cytotox_data(self) -> pd.DataFrame:
        """Получает все данные из домена Cytotox."""
        return self._get_and_parse("cytotox/data/all")

    def get_cytotox_column_stats(self) -> pd.DataFrame:
        """Получает статистику по колонкам для домена Cytotox."""
        return self._get_and_parse("cytotox/analytics/column-stats")

    def get_cytotox_row_stats(self) -> pd.DataFrame:
        """Получает статистику по строкам для домена Cytotox."""
        return self._get_and_parse("cytotox/analytics/row-stats")

    def get_cytotox_top_categories(self) -> pd.DataFrame:
        """Получает статистику по топовым категориям для домена Cytotox."""
        return self._get_and_parse("cytotox/analytics/top-categories")

    # --- Nanomag ---

    def get_nanomag_data(self) -> pd.DataFrame:
        """Получает все данные из домена Nanomag."""
        return self._get_and_parse("nanomag/data/all")

    def get_nanomag_column_stats(self) -> pd.DataFrame:
        """Получает статистику по колонкам для домена Nanomag."""
        return self._get_and_parse("nanomag/analytics/column-stats")

    def get_nanomag_row_stats(self) -> pd.DataFrame:
        """Получает статистику по строкам для домена Nanomag."""
        return self._get_and_parse("nanomag/analytics/row-stats")

    def get_nanomag_top_categories(self) -> pd.DataFrame:
        """Получает статистику по топовым категориям для домена Nanomag."""
        return self._get_and_parse("nanomag/analytics/top-categories")

    # --- Nanozymes ---

    def get_nanozymes_data(self) -> pd.DataFrame:
        """Получает все данные из домена Nanozymes."""
        return self._get_and_parse("nanozymes/data/all")

    def get_nanozymes_column_stats(self) -> pd.DataFrame:
        """Получает статистику по колонкам для домена Nanozymes."""
        return self._get_and_parse("nanozymes/analytics/column-stats")

    def get_nanozymes_row_stats(self) -> pd.DataFrame:
        """Получает статистику по строкам для домена Nanozymes."""
        return self._get_and_parse("nanozymes/analytics/row-stats")

    def get_nanozymes_top_categories(self) -> pd.DataFrame:
        """Получает статистику по топовым категориям для домена Nanozymes."""
        return self._get_and_parse("nanozymes/analytics/top-categories")

    # --- Seltox ---

    def get_seltox_data(self) -> pd.DataFrame:
        """Получает все данные из домена Seltox."""
        return self._get_and_parse("seltox/data/all")

    def get_seltox_column_stats(self) -> pd.DataFrame:
        """Получает статистику по колонкам для домена Seltox."""
        return self._get_and_parse("seltox/analytics/column-stats")

    def get_seltox_row_stats(self) -> pd.DataFrame:
        """Получает статистику по строкам для домена Seltox."""
        return self._get_and_parse("seltox/analytics/row-stats")

    def get_seltox_top_categories(self) -> pd.DataFrame:
        """Получает статистику по топовым категориям для домена Seltox."""
        return self._get_and_parse("seltox/analytics/top-categories")

    # --- Synergy ---

    def get_synergy_data(self) -> pd.DataFrame:
        """Получает все данные из домена Synergy."""
        return self._get_and_parse("synergy/data/all")

    def get_synergy_column_stats(self) -> pd.DataFrame:
        """Получает статистику по колонкам для домена Synergy."""
        return self._get_and_parse("synergy/analytics/column-stats")

    def get_synergy_row_stats(self) -> pd.DataFrame:
        """Получает статистику по строкам для домена Synergy."""
        return self._get_and_parse("synergy/analytics/row-stats")

    def get_synergy_top_categories(self) -> pd.DataFrame:
        """Получает статистику по топовым категориям для домена Synergy."""
        return self._get_and_parse("synergy/analytics/top-categories")