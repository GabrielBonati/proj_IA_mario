import retro
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv

def train_agent():
    # Configurações do ambiente Retro Gym
    env = retro.make(game='SuperMarioWorld-Snes', state='YoshiIsland1', players=1)
    env = DummyVecEnv([lambda: env])

    # Modelo DQN
    model = DQN("CnnPolicy", env, verbose=1)  # Pode ajustar a política e outros hiperparâmetros

    # Treinamento do agente
    model.learn(total_timesteps=int(1e5))  # Ajuste o número de etapas de treinamento conforme necessário

    # Salvando o modelo treinado
    model.save("mario_dqn_model")

if __name__ == "__main__":
    train_agent()
