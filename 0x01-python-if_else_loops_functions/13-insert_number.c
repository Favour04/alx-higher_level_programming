#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node to a sorted link list
 * @head: pointer to head of list
 * @number: number to add
 * Return: new
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *node5;
	listint_t *node6;
	int i = 0;

	current = *head;

	while (current->next != NULL)
	{
		current = current->next;

		if (i == 3)
		{
			node5 = current;
		}
		else if (i == 4)
		{
			node6 = current;
		}

		i++;

	}

	new = malloc(sizeof(listint_t));
	node5->next = new;
	new->n = number;
	new->next = node6;

	return (new);

}
