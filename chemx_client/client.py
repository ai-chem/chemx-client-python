# chemx_client/client.py

import requests
import pandas as pd
from typing import Optional, Dict, Any, List


class ChemXAPIError(Exception):
    """Кастомное исключение для ошибок, связанных с ChemX API."""
    pass


class ChemXClient:
    """
    Клиент для взаимодействия с API-сервером ChemX.
    """

    def __init__(self, base_url: str = "https://chemx-backend.onrender.com"):
        """
        Инициализирует клиент для работы с ChemX API.

        Args:
            base_url (str): Адрес запущенного сервера ChemX-backend.
        """
        self.base_url = f"{base_url.rstrip('/')}/api/v1"
        self.session = requests.Session()

    def _get_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Внутренний метод для выполнения GET-запроса и возврата JSON."""
        full_url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.get(full_url, params=params)
            response.raise_for_status()  # Вызовет ошибку для статусов 4xx/5xx
            return response.json()

        except requests.exceptions.HTTPError as e:
            raise ChemXAPIError(f"Ошибка от API ({e.response.status_code}) для {full_url}: {e.response.text}") from e
        except requests.exceptions.RequestException as e:
            raise ChemXAPIError(f"Ошибка сети или подключения к {full_url}: {e}") from e
        except ValueError:
            raise ChemXAPIError(f"Не удалось декодировать JSON от {full_url}. Ответ сервера: {response.text}")

    def _get_and_parse_df(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """Внутренний метод, который делает запрос и парсит результат в DataFrame."""
        # Убираем None значения из параметров, чтобы не отправлять их в URL
        request_params = {k: v for k, v in (params or {}).items() if v is not None}

        # Добавляем file_format=json, если его еще нет
        if 'file_format' not in request_params:
            request_params['file_format'] = 'json'

        data = self._get_request(endpoint=endpoint, params=request_params)
        return pd.DataFrame(data)

    def get_schema(self) -> Dict[str, List[str]]:
        """
        Получает схему доступных данных: список всех доменов и типов данных.

        Returns:
            Dict[str, List[str]]: Словарь с ключами 'available_domains' и 'available_data_types'.
        """
        return self._get_request("data/schema")

    def get_dataset(self, domain: str, data_type: str, nanoparticle: Optional[str] = None) -> pd.DataFrame:
        """
        Универсальный метод для получения любого датасета по его домену и типу.

        Args:
            domain (str): Имя домена (например, 'cytotox', 'nanomag').
            data_type (str): Тип данных (например, 'all_data', 'ml_data', 'column_stats').
            nanoparticle (str, optional): Фильтр по названию наночастицы.

        Returns:
            pd.DataFrame: Запрошенный датасет в виде DataFrame.
        """
        params = {
            "domain": domain,
            "data_type": data_type,
            "nanoparticle": nanoparticle,
        }
        return self._get_and_parse_df("data", params=params)

    # --- Старые, специфичные методы (остаются для обратной совместимости) ---

    # --- Cytotox ---
    def get_cytotox_data(self, nanoparticle: Optional[str] = None) -> pd.DataFrame:
        return self._get_and_parse_df("cytotox/data/all", params={"nanoparticle": nanoparticle})

    def get_cytotox_column_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("cytotox/analytics/column-stats")

    def get_cytotox_row_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("cytotox/analytics/row-stats")

    def get_cytotox_top_categories(self) -> pd.DataFrame:
        return self._get_and_parse_df("cytotox/analytics/top-categories")

    def get_cytotox_ml_data(self) -> pd.DataFrame:
        return self._get_and_parse_df("cytotox/data/ml")

    # --- Nanomag ---
    def get_nanomag_data(self, nanoparticle: Optional[str] = None) -> pd.DataFrame:
        return self._get_and_parse_df("nanomag/data/all", params={"nanoparticle": nanoparticle})

    def get_nanomag_column_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanomag/analytics/column-stats")

    def get_nanomag_row_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanomag/analytics/row-stats")

    def get_nanomag_top_categories(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanomag/analytics/top-categories")

    def get_nanomag_ml_data(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanomag/data/ml")

    # --- Nanozymes ---
    def get_nanozymes_data(self, nanoparticle: Optional[str] = None) -> pd.DataFrame:
        return self._get_and_parse_df("nanozymes/data/all", params={"nanoparticle": nanoparticle})

    def get_nanozymes_column_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanozymes/analytics/column-stats")

    def get_nanozymes_row_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanozymes/analytics/row-stats")

    def get_nanozymes_top_categories(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanozymes/analytics/top-categories")

    def get_nanozymes_ml_data(self) -> pd.DataFrame:
        return self._get_and_parse_df("nanozymes/data/ml")

    # --- Seltox ---
    def get_seltox_data(self, nanoparticle: Optional[str] = None) -> pd.DataFrame:
        return self._get_and_parse_df("seltox/data/all", params={"nanoparticle": nanoparticle})

    def get_seltox_column_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("seltox/analytics/column-stats")

    def get_seltox_row_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("seltox/analytics/row-stats")

    def get_seltox_top_categories(self) -> pd.DataFrame:
        return self._get_and_parse_df("seltox/analytics/top-categories")

    def get_seltox_ml_data(self) -> pd.DataFrame:
        return self._get_and_parse_df("seltox/data/ml")

    # --- Synergy ---
    def get_synergy_data(self, nanoparticle: Optional[str] = None) -> pd.DataFrame:
        return self._get_and_parse_df("synergy/data/all", params={"nanoparticle": nanoparticle})

    def get_synergy_column_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("synergy/analytics/column-stats")

    def get_synergy_row_stats(self) -> pd.DataFrame:
        return self._get_and_parse_df("synergy/analytics/row-stats")

    def get_synergy_top_categories(self) -> pd.DataFrame:
        return self._get_and_parse_df("synergy/analytics/top-categories")

    def get_synergy_ml_data(self) -> pd.DataFrame:
        return self._get_and_parse_df("synergy/data/ml")