import csv
from pysui import SuiConfig, SyncClient
from pysui.sui.sui_clients.sync_client import SuiClient
from pysui.sui.sui_types.address import SuiAddress


def generate_sui_wallets(num_wallets=50, output_file="sui_wallets.csv"):
    """生成 Sui 钱包并保存到 CSV 文件"""
    wallets = []

    for _ in range(num_wallets):
        # 生成新钱包配置（包含私钥和地址）
        config = SuiConfig.generate_new_config()

        # 提取私钥和地址
        private_key = config.private_key.key_pair.private_key.hex()
        address = config.active_address.address

        # 保存到列表
        wallets.append({
            "private_key": private_key,
            "address": address
        })

    # 写入 CSV 文件
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["private_key", "address"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(wallets)

    return wallets


if __name__ == "__main__":
    # 生成 50 个钱包
    wallets = generate_sui_wallets(50)

    # 打印示例结果
    print(f"成功生成 {len(wallets)} 个 Sui 钱包")
    print(f"示例钱包信息：")
    print(f"地址: {wallets[0]['address']}")
    print(f"私钥: {wallets[0]['private_key']}")
    print(f"结果已保存至 sui_wallets.csv")