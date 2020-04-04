CREATE TABLE categories (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(60) NOT NULL,
	description VARCHAR(100),
	UNIQUE (name)
);

CREATE TABLE orders (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	date TIMESTAMP(10) NOT NULL,
	CPF CHAR(11),
	CNPJ CHAR(14)
);

CREATE TABLE products (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(100) NOT NULL,
	description VARCHAR(400),
	value NUMERIC(8, 2) NOT NULL,
	picture VARCHAR(100),
	amount INTEGER NOT NULL DEFAULT 0,
	id_category INT NOT NULL,
	FOREIGN KEY (id_category) REFERENCES categories (id)
	UNIQUE (name)
);

CREATE TABLE items (
	id_order INTEGER NOT NULL,
	id_product INTEGER NOT NULL,
	number INTEGER NOT NULL,
	amount INTEGER NOT NULL,
	discount NUMERIC(8, 2),
	PRIMARY KEY (id_order, id_product),
	FOREIGN KEY (id_order) REFERENCES orders (id),
	FOREIGN KEY (id_product) REFERENCES products (id)
);

INSERT INTO categories (name) VALUES
	('Cereais'),
	('Latarias e Conservas'),
	('Massas'),
	('Congelados'),
	('Perfumaria'),
	('Bebidas'),
	('Açougue'),
	('Padaria'),
	('Adega'),
	('Churrascaria'),
	('Laticínios'),
	('Hortifrutis'),
	('Doces e chocolates');

INSERT INTO products (name, description, value, picture, amount, id_category) VALUES
	('Aveia em Flocos Nestlé 170g', 'É um alimento saudável e com alto teor de fibras. É feito com Cereal Integral, além de ser rico em fibras e proteínas. Experimente com frutas picadas ou amassadas, fica uma delícia!', 3.95, 'aveia_em_flocos_nestle_170g.png', 60, 1),
	('Carne Caldo Tablete Maggi Equilibrium 57g', 'O Caldo de Carne Maggi Equilibrium é muito bom para incrementar o sabor dos seus pratos. Além de versátil, apresenta 31% menos sódio que a versão regular.', 1.35, 'carne_caldo_tablete_maggi_equilibrium_57g.jpg', 200, 2),
	('Ketchup Hemmer Tradicional 1kg', 'Utilizado para realçar o sabor de variados pratos: assados, peixes, fritadas, arroz e salgadinhos. É presença quase obrigatória em comidas rápidas, como hambúrgueres e outros tipos de sanduíches, pastéis, pizzas, petiscos e batatas fritas. Porção de 12g (1 colher de sopa) = 12kcal.', 11.49, 'ketchup_hemmer_tradicional_1kg.jpg', 20, 2),
	('Óleo de Soja Liza Pet 900ml', 'Este óleo possui um equilíbrio de gorduras monoinsaturadas e é comumente utilizado na preparação de receitas culinárias ou até mesmo para fins cosméticos, fornecendo propriedades essenciais no funcionamento do organismo, dentre elas o auxílio em funções cardíacas e regulação do coleterol.', 3.99, 'oleo_de_soja_liza_pet_900ml.png', 250, 1),
	('Sal Refinado Cisne Pacote 1kg', 'Recomendado para diversas aplicações alimentícias, pode ser encontrado em embalagens variadas e também com teor de sódio reduzido, sempre seguindo rigorosamente a legislação de adição de iodo.', 2.29, 'sal_refinado_cisne_pacote_1kg.jpg', 100, 1),
	('Bebida Láctea Fermentada Sabor Morango Batavo 180g', 'Sabor e praticidade para o seu dia! Nossas Bebidas Lácteas Batavo são gostosas, práticas e prontas pra você levar contigo para onde for! Contém aromatizante sintético idêntico ao natural. Porção de 180g (1 unidade) = 140kcal.', 1.99, 'bebida_lactea_fermentada_sabor_morango_batavo_180g.png', 80, 4),
	('Arroz Agulhinha Tipo 1 Tio João Pacote 5kg', 'Um arroz branquinho, soltinho e saboroso é de dar água na boca. Com o arroz Tio João 100% Grãos Nobres é assim. Ele passa por um processo de seleção e beneficiamento de grãos, que deixa o arroz perfeito e com um excelente rendimento.', 19.49, 'arroz_agulhinha_tipo_1_tio_joao_pacote_5kg.png', 80, 1),
	('Leite em Pó Integral Instantâneo Piracanjuba 800g Pouch', 'Leite Em Pó Integral Instantâneo Piracanjuba 800g Rico em ferro, Zinco e vitaminas A C D. Ingredientes: Leite integral, mix de minerais ferro e zinco e vitaminas A, C e D e emulsificante lecitina de soja. Alérgicos: Contém leite e derivados de soja. Contém lactose, não contém glúten.', 16.65, 'leite_em_po_integral_instantaneo_piracanjuba_800g_pouch.jpg', 120, 2),
	('Macarrão de Sêmola Espaguete Galo 500g', 'O produto tem como destaque sua tradicional fórmula com trigo, clara de ovos e monocloridrato de L-Lisina, o que permite uma refeição saudável.', 1.80, 'macarrao_de_semola_espaguete_galo_500g.png', 40, 3),
	('Farinha de Trigo Tradicional Dona Benta Pacote 1kg', 'Seu aspecto é esbranquiçado e macio, e seu aroma sutil, podendo servir como ingrediente para incontáveis receitas doces ou salgadas, e seu consumo moderado proporciona melhorias no organismo como regulação do colesterol ruim e fornecimento de energia. Contém Glúten.', 3.99, 'farinha_de_trigo_tradicional_dona_benta_pacote_1kg.png', 60, 1);

INSERT INTO orders (date, CPF) VALUES
	('2020-03-15 10:03:30', '46767218030'),
	('2020-03-15 10:05:29', '95745723076'),
	('2020-03-15 10:15:32', '48259400057'),
	('2020-03-15 11:13:02', '71044098074'),
	('2020-03-15 11:22:31', '03059228078'),
	('2020-03-15 11:34:27', '84612964004'),
	('2020-03-15 11:38:42', '11802899006'),
	('2020-03-15 11:55:35', '65111301003');

INSERT INTO items (id_order, id_product, number, amount, discount) VALUES
	(1, 1, 2, 1, 0.0),
	(1, 2, 5, 2, 0.0),	
	(2, 1, 8, 3, 0.0),
	(2, 2, 9, 1, 0.0),
	(2, 3, 10, 3, 0.0),	
	(3, 1, 6, 5, 0.71),	
	(4, 1, 4, 1, 0.0),
	(4, 2, 10, 1, 0.0),	
	(5, 1, 3, 2, 0.0),
	(5, 2, 1, 2, 0.0),
	(5, 3, 2, 4, 0.0),
	(5, 4, 5, 1, 0.0),	
	(6, 1, 1, 2, 0.0),	
	(6, 2, 4, 5, 0.0),	
	(7, 1, 6, 2, 0.0),
	(7, 2, 8, 1, 0.0),
	(7, 3, 1, 3, 0.0),	
	(8, 1, 2, 2, 0.0);


--https://www.supermercadocampestre.com.br/index.php/secoes
