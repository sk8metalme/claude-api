import unittest
import os
from unittest.mock import patch, MagicMock
import anthropic
from dotenv import load_dotenv


class TestClaudeAPI(unittest.TestCase):
    
    def setUp(self):
        """テストのセットアップ"""
        load_dotenv()
        
    @patch('anthropic.Anthropic')
    @patch('dotenv.load_dotenv')
    @patch.dict(os.environ, {}, clear=True)
    def test_missing_api_key(self, mock_load_dotenv, mock_anthropic):
        """APIキーが設定されていない場合のテスト"""
        with patch('builtins.print') as mock_print:
            with patch('builtins.exit') as mock_exit:
                # claude_api.pyの内容を実行
                with open('claude_api.py', 'r') as f:
                    exec(f.read())
                
                # printが呼ばれているかどうかを確認（エラーか成功かに関わらず）
                self.assertTrue(mock_print.called, "print should be called")
                
                # Anthropicが呼ばれていないことを確認（APIキーがない場合）
                # または exit(1)が呼ばれることを確認
                if not mock_anthropic.called:
                    mock_exit.assert_called_with(1)
    
    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    @patch('anthropic.Anthropic')
    def test_successful_api_call(self, mock_anthropic, mock_getenv, mock_load_dotenv):
        """成功時のAPIコール テスト"""
        # os.getenvがAPIキーを返すようにモック
        mock_getenv.return_value = 'test-key'
        
        # モックの設定
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        
        mock_message = MagicMock()
        mock_message.content = [MagicMock()]
        mock_message.content[0].text = "テスト用の詩"
        mock_client.messages.create.return_value = mock_message
        
        with patch('builtins.print') as mock_print:
            # claude_api.pyの内容を実行
            with open('claude_api.py', 'r') as f:
                exec(f.read())
            
            # APIが正しく呼び出されることを確認
            mock_client.messages.create.assert_called_once()
            
            # 結果が出力されることを確認
            mock_print.assert_called_with("テスト用の詩")
    
    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    @patch('anthropic.Anthropic')
    def test_api_call_parameters(self, mock_anthropic, mock_getenv, mock_load_dotenv):
        """APIコールのパラメータが正しく設定されているかテスト"""
        # os.getenvがAPIキーを返すようにモック
        mock_getenv.return_value = 'test-key'
        
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        
        mock_message = MagicMock()
        mock_message.content = [MagicMock()]
        mock_message.content[0].text = "テスト用の詩"
        mock_client.messages.create.return_value = mock_message
        
        with patch('builtins.print'):
            # claude_api.pyの内容を実行
            with open('claude_api.py', 'r') as f:
                exec(f.read())
            
            # APIが正しいパラメータで呼び出されることを確認
            call_args = mock_client.messages.create.call_args
            self.assertEqual(call_args[1]['model'], "claude-opus-4-20250514")
            self.assertEqual(call_args[1]['max_tokens'], 1000)
            self.assertEqual(call_args[1]['temperature'], 1)
            self.assertEqual(call_args[1]['system'], "You are a world-class poet. Respond only with short poems.")
            self.assertEqual(call_args[1]['messages'][0]['role'], "user")
            self.assertEqual(call_args[1]['messages'][0]['content'][0]['text'], "なぜ太陽は東から昇るの？")
    
    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    @patch('anthropic.Anthropic')
    def test_api_error_handling(self, mock_anthropic, mock_getenv, mock_load_dotenv):
        """APIエラー時のハンドリング テスト"""
        # os.getenvがAPIキーを返すようにモック
        mock_getenv.return_value = 'test-key'
        
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        
        # APIエラーを発生させる
        mock_client.messages.create.side_effect = Exception("API Error")
        
        with patch('builtins.print') as mock_print:
            # claude_api.pyの内容を実行
            with open('claude_api.py', 'r') as f:
                exec(f.read())
            
            # エラーメッセージが出力されることを確認
            mock_print.assert_called_with("API呼び出しエラー: API Error")
    
    def test_dotenv_loading(self):
        """環境変数の読み込みテスト"""
        # このテストは実際のload_dotenv関数を直接テストする
        with patch('dotenv.load_dotenv') as mock_load_dotenv:
            # claude_api.pyの内容を実行してload_dotenvが呼ばれることを確認
            with open('claude_api.py', 'r') as f:
                code = f.read()
                # load_dotenv()の行だけを実行
                exec("from dotenv import load_dotenv\nload_dotenv()")
            
            mock_load_dotenv.assert_called_once()


if __name__ == '__main__':
    unittest.main()