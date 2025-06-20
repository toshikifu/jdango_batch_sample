# jdango-batch-sample

このプロジェクトは、Django と Celery を用いたバッチ処理のサンプルです。Docker 環境で Django アプリケーション、Celery ワーカー、タスク監視用 Flower、Redis、MySQL を簡単に立ち上げて動作確認できます。

## 必要要件

- Docker
- Docker Compose

## セットアップ方法

1. リポジトリをクローンします。
2. 以下のコマンドでサービスを起動します。

```bash
docker-compose up --build
```

初回起動時はマイグレーションも自動で実行されます。

## サービス構成

- **app**: Django アプリケーション (開発サーバー)
- **celery**: Celery ワーカー
- **monitor**: Flower (Celery タスク監視 UI)
- **db**: MySQL (開発用)
- **redis**: Redis (Broker/キャッシュ)

## 各種サービスへのアクセス

- Django 管理画面: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Flower: [http://localhost:5555/](http://localhost:5555/)

## サンプルバッチタスク

`polls/tasks.py` にサンプルタスクが定義されています。

- `hello_world(name)` : 名前付きで Hello World を出力
- `calc(a, b)` : 2 つの数値を加算
- `time_sleep_func(project_id)` : 10 秒スリープ後に完了メッセージを返す

## Django 管理コマンドからのバッチ実行例

### hello_world_queue

```bash
docker-compose exec app uv run manage.py hello_world_queue --name=テスト --num=3
```

- `--name` : 挨拶する名前
- `--num` : タスクを何件キューに積むか

### time_sleep_cmd

```bash
docker-compose exec app uv run manage.py time_sleep_cmd
```

- 10 秒スリープするバッチタスクを実行し、結果を DB から取得して表示します。

## ディレクトリ構成

```
celery_app/
  config/         # Django設定・Celery設定
  polls/          # サンプルアプリ・バッチタスク/コマンド
  main.py         # サンプルエントリポイント
  manage.py       # Django管理コマンド
  Dockerfile      # アプリ用Dockerfile
pyproject.toml    # 依存パッケージ定義
README.md         # このファイル
```

## 補足

- Celery の Broker/Backend には Redis と DB（django-celery-results）を利用しています。
- Flower でタスクの状態や履歴を Web UI で確認できます。
- サンプルのため、セキュリティや本番運用は考慮していません。
